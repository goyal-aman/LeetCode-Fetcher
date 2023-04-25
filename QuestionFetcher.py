import requests
from bs4 import BeautifulSoup
import mistune

# Get the name of the problem from the user
class QuestionFetcher:

    def get_question_html(name: str):
        # name = input("Enter the name of the LeetCode problem: ")

        # Make a GET request to the problem page and parse the HTML using BeautifulSoup
        url = f"https://leetcode.com/problems/{name}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the element with 'data-track-load' property = 'qd_description_content'
        description_elem = soup.find(attrs={'data-track-load': 'qd_description_content'})

        # Get the HTML content of the description element and convert it to Markdown
        description_html = description_elem.decode_contents()
        return description_html
    
    def html_to_md(html_str: str):
        description_markdown = mistune.html(html_str)
        return description_markdown
    
    def save_to_md(filename: str, markdown_file_content:str, header=None):
        # Write the Markdown content to a file
        # filename = f"{name}.md"

        if header is None:
            header = filename

        with open(filename, "w") as f:
            f.write(f"#{header}\n")
            f.write("")
            f.write(markdown_file_content)

        print(f"Description saved to {filename}")
    
    def execute(question_name: str, file_path: str = None):

        if file_path is None:
            file_path = question_name

        html = QuestionFetcher.get_question_html(question_name)
        md = QuestionFetcher.html_to_md(html)
        QuestionFetcher.save_to_md(f"{file_path}.md", md, QuestionFetcher.clean_name(question_name))


    def clean_name(name:str):
        return name.replace("-", " ").title()

if __name__ == "__main__":
    question_name = "same-tree"
