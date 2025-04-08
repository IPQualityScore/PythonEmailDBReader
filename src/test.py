import unittest
from unittest.mock import patch
from util.emaillookup.emaillookup import EmailLookup

 # this class contains a testing of each of the libs functions.
class TestEmailLookup(unittest.TestCase):        

    @patch.object(EmailLookup, 'lookupEmail') # Tests a flatfile lookup
    def testDomain(self, mock_lookup):
        # To use python3 -m unittest test.py
        mock_lookup.return_value = None
        instance = EmailLookup(path="src/test/sample/domain-flat-file-sample-0.bin")
        email = "example@ipqualityscore.com"
        result = instance.lookupEmail(email)
        self.assertIsNone(result, "Result is none!")
        mock_lookup.return_value = "true"
        result = instance.lookupEmail(email)
        self.assertEqual(result, "true") 

    @patch.object(EmailLookup, 'lookupEmail')
    def testEmail(self, mock_lookup): # Tests a email lookup
        # To use python3 -m unittest test.py
        mock_lookup.return_value = None
        instance = EmailLookup(path="src/tree/tree-test-working-0.bin")
        for i in range(10000):
            email = f"{i}@example.com"
            result = instance.lookupEmail(email)
            self.assertIsNone(result, "Result is none!")
        mock_lookup.return_value = "true"
        for i in range(10000):
            email = f"{i}@example.com"
            result = instance.lookupEmail(email)
            self.assertEqual(result, "true")
    
    @patch.object(EmailLookup, 'lookupEmail') # Test a email lookup tree
    def testTreeTrue(self, mock_lookup):
        # To use python3 -m unittest test.py
        mock_lookup.return_value = None
        instance = EmailLookup(path="src/tree/tree-test-email-0.bin")
        def lookupMailSim(email):
            if email.endswith("@example.com"):
                return "true"
            return None
        mock_lookup.side_effect = lookupMailSim
        email = None
        for i in range(10000):
            email = f"{i}@example.com"
            result = instance.lookupEmail(email)
            self.assertIsNotNone(result, f"Value is none {email}!")
        mock_lookup.return_value = "true"
        if email:
            result = instance.lookupEmail(email)
            self.assertEqual(result, "true")

    @patch.object(EmailLookup, 'lookupEmail')    # Lookup test tree data fail
    def testTreeFail(self, mock_lookup):
        # To use python3 -m unittest test.py
        mock_lookup.return_value = None
        instance = EmailLookup(path="src/tree/tree-test-email-0.bin")
        def lookupMailSim(email):
            if email.endswith("@example.com"):
                return "false"
            return None
        mock_lookup.side_effect = lookupMailSim
        email = None
        for i in range(10000):
            email = f"{i}@example.com"
            result = instance.lookupEmail(email)
            self.assertIsNotNone(result, f"Value is none {email}!")
        mock_lookup.return_value = "false"
        if email:
            result = instance.lookupEmail(email)
            self.assertEqual(result, "false")

