import unittest
from ..new_articles import clean, get_paragraphs


class Clean(unittest.TestCase):
    def test_clean(self):
        """test that the clean function removes " from a string"""
        str_to_clean = "\"test\""

        result = clean(str_to_clean)
        expectation = "test"

        self.assertEqual(result, expectation)

    def test_get_paragraphs(self):
        """test that get_paragraphs gets 4 paragraphs"""
        with open('mock_article') as file:
            bbc_article = file.readline()

        formatted_bbc_article = bbc_article.split('\', \'')

        result = len(get_paragraphs(formatted_bbc_article))
        expectation = 4

        self.assertEqual(result, expectation)


if __name__ == '__main__':
    unittest.main()
