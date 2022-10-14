from bs4 import BeautifulSoup
from utils.utils import Utils
from models.fixture import Fixture


class ScrapeService:

    @staticmethod
    def scrape_next_match_page(url: str):
        url = "https://www.slbenfica.pt/pt-pt/jogos/calendario"
        page_html = Utils.execute_get_request(url).text
        soup = BeautifulSoup(page_html, "lxml")
        fixture = Fixture(None, None, None, None, None, None, None)
        if soup:
            for div in soup.find_all("div", {"class": "wrapper-highlight-event row"}):
                for sub_div in div.find_all("div", {"class": "highlight-event-team col-md-5 text-right"}):
                    fixture.home_img = sub_div.find("img")['src']
                    fixture.home = sub_div.find_all("div", {"class": "highlight-event-team-name"})[0].contents[0]

                for sub_div in div.find_all("div", {"class": "highlight-event-team col-md-5 text-left"}):
                    fixture.away_img = sub_div.find("img")['src']
                    fixture.away = sub_div.find_all("div", {"class": "highlight-event-team-name"})[0].contents[0]

                for sub_div in div.find_all("div", {"class": "highlight-event-center col-md-2"}):
                    fixture.competition = sub_div.contents[1].contents[0]
                    fixture.date = sub_div.contents[3].contents[0]
                    fixture.kick_off = sub_div.contents[5].contents[0]

        return fixture
