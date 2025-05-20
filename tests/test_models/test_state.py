#!/usr/bin/python3
"""Defines unnittests for models/state.py."""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    # def test_attributes(self):
    #     """Check for attributes."""
    #     st = State(name="a")
    #     self.assertEqual(str, type(st.id))
    #     self.assertEqual(datetime, type(st.created_at))
    #     self.assertEqual(datetime, type(st.updated_at))
    #     self.assertTrue(hasattr(st, "name"))

    def test_is_subclass(self):
        """Check that State is a subclass of BaseModel."""
        self.assertTrue(issubclass(State, BaseModel))

    def test_name(self):
        """Test that State has attr name, and it's an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
        
        # Test name assignment
        state.name = "state name"
        self.assertEqual(state.name, "state name")




if __name__ == "__main__":
    unittest.main()