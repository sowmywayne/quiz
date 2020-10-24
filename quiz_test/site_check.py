import unittest
import requests

class TestQuiz(unittest.TestCase):
  def test_home_url(self):
    result = requests.get("http://sowmywayne.pythonanywhere.com")
    self.assertEqual(result.status_code, 200)

  def test_test_url(self):
    result = requests.get("http://sowmywayne.pythonanywhere.com/test")
    self.assertEqual(result.status_code, 200)


if __name__ == "__main__":
  unittest.main()
    