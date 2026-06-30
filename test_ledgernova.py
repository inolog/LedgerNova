# test_ledgernova.py
"""
Tests for LedgerNova module.
"""

import unittest
from ledgernova import LedgerNova

class TestLedgerNova(unittest.TestCase):
    """Test cases for LedgerNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerNova()
        self.assertIsInstance(instance, LedgerNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
