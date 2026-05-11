import loguru
from loguru import logger
from configparser import *
import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\nabaj\OneDrive\Desktop\STUDY_Python\DE_Project_Nabajyoti\config_file.ini")

# one step method
book_price=config["bookcost"]["science"]
print(book_price)

# Two steo method
book_price=config["bookcost"]
print(book_price["science"])






# student_name_and_books = {
#     1: ["math", "language", "polity"],
#     2: ["biology", "science"],
#     3: ["math", "computer"],
#     4: ["language", "science", "computer","geography"]
# }

# for student_id in student_name_and_books:
#     book_list=student_name_and_books[student_id]
#     Total_cost=0
#     for book_name in book_list:
#         Total_cost = Total_cost + float(config["bookcost"][book_name])
        
#     logger.info(f"cost spent by student : {student_id} is {Total_cost}")
    


