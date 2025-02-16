import os
import pandas as pd


class BaseEngin:
    FILE_DIR = "exel_db"
    FILE_DB = "data.xlsx"

    def __init__(self):
        self.filepath = os.path.join(self.FILE_DIR, self.FILE_DB)

        if not os.path.exists(self.FILE_DIR):
            os.makedirs('exel_db', exist_ok=True)
            print("Create directory exel_db")

    def write(self, word1: str, word2: str):
        if not os.path.exists(self.filepath):  # при начале работы, когда нет файла
            print("NOT FILE")
            df = pd.DataFrame()  # создали пустой датафрейм
        else:
            df = pd.read_excel(self.filepath)
        # Добавляем строку посредством словаря (параметр ignore_index=True нужен для сохранения порядка)
        df = df._append(
            {'word1': word1, 'word2': word2}, ignore_index=True
        )

        df.to_excel(self.filepath, index=False)  # index=False, что бы не появлялись колонки <Unnamed: 0>

    def read(self):
        list_result = list()
        if not os.path.exists(self.filepath):  # при начале работы, когда нет файла
            print("NOT FILE")
            return
        df = pd.read_excel(self.filepath)

        for i in range(len(df)):
            line = df.loc[i]
            key, value = line["word1"], line["word2"]
            list_result.append([key, value])
        return list_result


if __name__ == "__main__":
    a = BaseEngin()
    # a.write("mother", "father")
    # a.write("very", "match")
    a.read()
