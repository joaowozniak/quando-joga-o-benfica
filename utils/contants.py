class Constants:

    @staticmethod
    def weekly_show_endpoint(show_id: str) -> str:
        return "https://bandcamp.com/?show=" + str(show_id)
