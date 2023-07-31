if __name__ == "__main__":
        text = input("Enter a text: ");
        for i in range(len(text)):
                if text[i] not in text[:i]:
                        print(f"{text[i]}:{text.count(text[i])}");