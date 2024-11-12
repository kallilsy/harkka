from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        data = tomli.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        return Project(
            name=data.get("name", "Unnamed Project"),
            description=data.get("description", "No description available"),
            dependencies=data.get("dependencies", []),
            dev_dependencies=data.get("dev-dependencies", [])
        )