class Config:
    APP_NAME = "Эмоции Трекер"
    REPORT_FILE = "emotion_report.txt"
    DATE_FORMAT = "%d.%m.%Y %H:%M:%S"
    EMOTION_LIST = ["Радость", "Грусть", "Спокойствие"]

    @staticmethod
    def get_report_path() -> str:
        return Config.REPORT_FILE

    @staticmethod
    def get_date_format() -> str:
        return Config.DATE_FORMAT

    @staticmethod
    def get_emotions() -> list:
        return Config.EMOTION_LIST.copy()