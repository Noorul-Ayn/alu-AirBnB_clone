#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_str_uuid(self):
        self.assertIsInstance(self.model.id, str)
        # Check if id is a valid UUID
        try:
            uuid_obj = uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid uuid4 string")

    def test_created_at_and_updated_at_are_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict_returns_dict(self):
        d = self.model.to_dict()
        self.assertIsInstance(d, dict)
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], self.model.id)
        self.assertEqual(d["created_at"], self.model.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.model.updated_at.isoformat())

    def test_str_representation(self):
        s = str(self.model)
        self.assertIn("BaseModel", s)
        self.assertIn(self.model.id, s)

    def test_dynamic_attributes(self):
        self.model.name = "Test"
        self.model.value = 42
        d = self.model.to_dict()
        self.assertEqual(d["name"], "Test")
        self.assertEqual(d["value"], 42)


if __name__ == "__main__":
    unittest.main()
