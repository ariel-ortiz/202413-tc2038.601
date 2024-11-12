
def find(s: str, words: set[str], answer: list[str] = []) -> list[str] | None:
    if s == '':
        return answer
    index: int = 0
    word: str = ''
    while index < len(s):
        word += s[index]
        if word in words:
            new_answer: list[str] | None = find(s[index + 1:], words, answer + [word])
            if new_answer is not None:
                return new_answer
        index += 1
    return None


if __name__ == '__main__':
    words: set[str] = {
        'the', 'a', 'an', 'boy', 'girl',
        'dog', 'ran', 'ate', 'homework',
        'table', 'them', 'my', 'kissed'
    }
    print(find('thedog', words))
    print(find('thedogatemyhomework', words))
    print(find('thegirlkissedtheboy', words))
