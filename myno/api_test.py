import unittest
import requests

class APITestCase(unittest.TestCase):
    def test_get_word(self):
        response = requests.get('http://localhost:5000/api/word')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('word', data)

    def test_update_word(self):
        new_word = 'New Test Word'
        payload = {'word': new_word}
        response = requests.post('http://localhost:5000/admin/update', json=payload)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Word updated successfully')

if __name__ == '__main__':
    unittest.main()
