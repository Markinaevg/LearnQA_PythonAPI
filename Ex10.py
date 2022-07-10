class Test_EX10:
    def test_shortphrase(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) <= 15, f'Фраза "{phrase}" длиннее разрешенных 15 символов!'
        print(f'Введенная фраза "{phrase}" подходит под условие задачи! Длина фразы - {len(phrase)}')

