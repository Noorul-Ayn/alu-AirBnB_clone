#!/usr/bin/python3
import os
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    
    @classmethod
    def setUp(self):
        """Set up test cases."""
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass
    
    @classmethod
    def tearDown(self):
        """Clean up after test cases."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass
        FileStorage._FileStorage__objects = {}
    
    def test_all(self):
        """Test that all returns the __objects dictionary."""
        self.assertEqual(dict, type(storage.all()))
        self.assertIs(storage.all(), storage._FileStorage__objects)
    
    def test_all_with_arg(self):
        """Test all method with arguments."""
        with self.assertRaises(TypeError):
            storage.all(None)
    
    def test_new(self):
        """Test that new adds an object to the __objects dictionary."""
        bm = BaseModel()
        storage.new(bm)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], bm)
    
    def test_new_with_args(self):
        """Test new method with invalid arguments."""
        with self.assertRaises(TypeError):
            storage.new(BaseModel(), 1)
    
    def test_new_with_None(self):
        """Test new method with None."""
        with self.assertRaises(AttributeError):
            storage.new(None)
    
    def test_save(self):
        """Test that save properly serializes objects to JSON file."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        with open("file.json", "r") as f:
            contents = f.read()
            self.assertIn(f"BaseModel.{bm.id}", contents)
            self.assertIn("created_at", contents)
            self.assertIn("updated_at", contents)
            self.assertIn("id", contents)
    
    def test_save_with_arg(self):
        """Test save method with argument."""
        with self.assertRaises(TypeError):
            storage.save(None)
    
    def test_save_with_self(self):
        """Test save method with self as argument."""
        with self.assertRaises(TypeError):
            storage.save(self)
    
    def test_reload(self):
        """Test that reload properly deserializes the JSON file to __objects."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        bm_id = bm.id
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertIn(f"BaseModel.{bm_id}", storage.all())
    
    def test_reload_with_arg(self):
        """Test reload method with argument."""
        with self.assertRaises(TypeError):
            storage.reload(None)
    
    def test_reload_from_nonexistent_file(self):
        """Test reload with a nonexistent file."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.assertEqual(storage.reload(), None)
    
    def test_reload_with_empty_file(self):
        """Test reload with an empty file."""
        # Clear the objects dictionary first
        FileStorage._FileStorage__objects = {}
        # Write empty JSON directly instead of calling save()
        with open("file.json", "w") as f:
            f.write("{}")
        storage.reload()
        self.assertEqual(storage.all(), {})
        
    def test_type_of_objects_after_reload(self):
        """Test that reloaded objects are of the correct type."""
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        bm_id = bm.id
        storage._FileStorage__objects = {}
        storage.reload()
        self.assertTrue(len(storage.all()) > 0)
        for obj in storage.all().values():
            self.assertEqual(type(obj), BaseModel)