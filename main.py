import csv
import random

def load_words(filename):
    words = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row_num, row in enumerate(reader, start=1):
            if len(row) < 4:
                print(f"Warning: Row {row_num} has insufficient columns: {row}")
                continue
            try:
                words.append({
                    'chinese': row[1].strip(),
                    'pinyin': row[2].strip(),
                    'english': row[3].strip()
                })
            except IndexError:
                print(f"Error in row {row_num}: {row}")
                continue
    if not words:
        raise ValueError("No valid words found in the CSV file")
    return words

def select_random_words(words, count=10):
    return random.sample(words, min(count, len(words)))

def display_words(selected_words):
    print("\nYour 10 random words for practice:\n")
    print(f"{'Chinese':<10} {'Pinyin':<15} {'English':<20}")
    print("-" * 45)
    for word in selected_words:
        print(f"{word['chinese']:<10} {word['pinyin']:<15} {word['english']:<20}")

def main():
    try:
        words = load_words('wordlist.csv')
        selected_words = select_random_words(words)
        display_words(selected_words)
    except FileNotFoundError:
        print("Error: wordlist.csv file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()