class InstantiateCSVError(KeyError):

    def __init__(self, *args):
        self.file_name = args[0] if args else None

    def __str__(self):
        return f"Файл {self.file_name} повреждён"
