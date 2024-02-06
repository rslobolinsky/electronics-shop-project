import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.massage = 'Файл поврежден'

    def __str__(self):
        return self.massage
