# import time
# from csv import reader, writer
#
# import os
#
#
# class DatasetAddition:
#
#     def read_csv(self, path="../news_csv_files/news_2019-07.csv"):
#         """read the url from the published article csv"""
#         file_path = os.path.abspath(path)
#         with open(file_path, 'r') as read_obj:
#             csv_reader = reader(read_obj)
#             for row in csv_reader:
#                 write_csv(row)
#                 time.sleep(1.1)
#
#     def write_csv(self, row):
#         """write text of article to bbcArticles.txt file"""
#         url_without_id = row[1].rsplit("-", 1)[0]
#         topic = url_without_id.split("/")[2]
#         print('topic', topic)
#         url = "https://www.bbc.co.uk" + row[1]
#         bbc_article = BBCArticle(url)
#         bbc_article_body = bbc_article.body
#         paragraphs = get_paragraphs(bbc_article_body)
#         rest_of_article = get_rest_of_article(bbc_article_body)
#         file_path = os.path.abspath("../datasets/testArticles.csv")
#         with open(file_path, mode='a') as articles_dataset:
#             articles_writer = writer(articles_dataset, delimiter=',')
#             article = [topic,
#                        paragraphs[0], paragraphs[1], paragraphs[2], paragraphs[3],
#                        rest_of_article]
#             articles_writer.writerow(article)
#
#     def get_rest_of_article(self, bbc_article):
#         """gets the text of the rest of the article"""
#         rest_of_article = str(bbc_article[6:-3])
#         clean_rest_of_article = clean(rest_of_article)
#         return clean_rest_of_article
#
#     def get_paragraphs(self, bbc_article):
#         """gets the first 4 paragraphs of the article"""
#         paragraph1 = clean(str(bbc_article[2]))
#         paragraph2 = clean(str(bbc_article[3]))
#         paragraph3 = clean(str(bbc_article[4]))
#         paragraph4 = clean(str(bbc_article[5]))
#         paragraphs = paragraph1, paragraph2, paragraph3, paragraph4
#         return paragraphs
#
#     def clean(self, str_to_clean):
#         """removes the " character from a string """
#         return str_to_clean.translate({ord(char): None for char in '"'})
