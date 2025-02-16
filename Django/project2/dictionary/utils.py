class AddWord:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    def __call__(self):
        print(self.word1, self.word2)


if __name__ == "__main__":
    a = AddWord("hello", "привет")
    a()
