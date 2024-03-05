import unittest
from binfileviz import process_file

class TestFileProcessing(unittest.TestCase):
    def test_file_to_binary_array(self):
        # Mock or use a test file with known content
        test_file_path = './Bin.txt'
        # Assuming process_file returns the binary array for this example
        binary_array = process_file(test_file_path)
        
        # Verify the binary_array contents
        expected_array = [1, 0, 1, 1, ...] # Expected result based on the test file
        self.assertEqual(binary_array, expected_array)

if __name__ == '__main__':
    unittest.main()
