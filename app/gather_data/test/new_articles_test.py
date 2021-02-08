import unittest
from ..new_articles import clean, get_paragraphs, get_rest_of_article


class TestBBCArticle(unittest.TestCase):
    """tests the methods within new_articles file"""
    def test_clean(self):
        """test that the clean function removes " from a string"""
        str_to_clean = "\"test\""

        result = clean(str_to_clean)
        expectation = "test"

        self.assertEqual(result, expectation)

    def test_get_paragraphs_length(self):
        """test that get_paragraphs gets 4 paragraphs"""

        bbc_article = ["reporter", "reporter info", "p1", "p2", "p3", "p4", "p5"]

        result = len(get_paragraphs(bbc_article))
        expectation = 4

        self.assertEqual(result, expectation)

    def test_get_4_paragraphs_text(self):
        """test that get_paragraphs gets the first 4 paragraphs of an article"""
        bbc_article = ["reporter", "reporter info", "p1", "p2", "p3", "p4", "p5"]

        result = get_paragraphs(bbc_article)
        expectation = ["p1", "p2", "p3", "p4"]

        self.assertEqual(result[0], expectation[0])
        self.assertEqual(result[1], expectation[1])
        self.assertEqual(result[2], expectation[2])
        self.assertEqual(result[3], expectation[3])

    def test_get_rest_of_article(self):
        """test that get_rest_of_article gets the text of the paragraphs after the first 4"""
        bbc_article = ["reporter", "reporter info", "p1", "p2", "p3", "p4",
                       "roa p5", "roa p6", "roa p7",
                       "related topics", "more on this story", "related articles"]

        result = get_rest_of_article(bbc_article)
        print(result)
        expectation = "['roa p5', 'roa p6', 'roa p7']"

        self.assertEqual(result, expectation)


if __name__ == '__main__':
    unittest.main()
