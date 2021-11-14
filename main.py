import time
import requests


class SoApi:
    @staticmethod
    def get_recent_questions(tag: str, last_days: int):
        url = "https://api.stackexchange.com/2.3/questions"
        params = {
            "page": 1,
            "pagesize": 50,
            "fromdate": int(time.time()) - last_days * 24 * 60 * 60,
            "order": "desc",
            "sort": "activity",
            "tagged": tag,
            "site": "stackoverflow"
        }
        response = requests.get(url=url, params=params).json()
        questions = []
        while True:
            for item in response["items"]:
                link = item["link"]
                title = item["title"]
                question = {
                    "link": link,
                    "title": title
                }
                questions.append(question)
            if response["has_more"]:
                params["page"] += 1
                response = requests.get(url=url, params=params).json()
            else:
                break
        return questions

    @staticmethod
    def print_questions(questions, tag: str, last_days: int):
        print(f"Список вопросов по тегу \"{tag}\" за последние(-ий) {last_days} дней(день, дня):")
        for question in questions:
            print("- " + question['title'])
            print("  " + question['link'])


if __name__ == '__main__':
    tag = "Python"
    last_days = 2
    questions = SoApi.get_recent_questions(tag, last_days)
    SoApi.print_questions(questions, tag, last_days)

