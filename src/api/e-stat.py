
class EStat:
	__url = "https://api.e-stat.go.jp/rest"
	def __init__(self, version: str, app_id: str) -> None:
		self.__version = version
		self.__app_id = app_id
	def get_url(self) -> str:
		return f'{self.__url}/{self.__version}/app/getStatsData'