from ujson import dump, load
from utils.path import file_exists

class Configuration():
    def __init__(self, file_name:str, cfg:dict = {}):
        self._config_file_name = file_name
        self._configuration = cfg

        if len(self._configuration) == 0:
            if file_exists(self._config_file_name):
                self.load_from_file()
        else:
            self.save_to_file()

    def __str__(self) -> dict:
        return self._configuration

    @property
    def configuration(self):
        return self._configuration

    @property
    def config_file_name(self):
        return self._config_file_name

    @property
    def keys(self):
        return self._configuration.keys()
    
    @property
    def values(self):
        return self._configuration.values()
    
    @property
    def items(self):
        return self._configuration.items()

    def load_from_file(self):
        if file_exists(self._config_file_name):
            with open(self._config_file_name, "r") as config_file:
                self._configuration = load(config_file)

    async def load_from_file_async(self):
        self.load_from_file()

    def save_to_file(self):
        with open(self._config_file_name, "w") as config_file:
            dump(self._configuration, config_file)

    async def save_to_file_async(self):
        self.save_to_file()

    def add(self, key:str, value):
        self._configuration[key] = value
        self.save_to_file()

    async def add_async(self, key:str, value):
        self._configuration[key] = value
        await self.save_to_file_async()

    def get(self, key:str):
        if key in self._configuration.keys():
            return self._configuration[key]   

        return None

    def update(self, key:str, value):
        self._configuration[key] = value
        self.save_to_file()

    async def update_async(self, key:str, value):
        self._configuration[key] = value
        await self.save_to_file_async()

    def remove(self, key:str):
        if key in self._configuration.keys():
            del self._configuration[key]
            self.save_to_file()
    
    async def remove_async(self, key:str):
        if key in self._configuration.keys():
            del self._configuration[key]
            await self.save_to_file_async()