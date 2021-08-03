class Singleton:
    _instance = None

    @classmethod
    def getInstance(cls):
        if Singleton._instance:
            return Singleton._instance
        else:
            return Singleton()