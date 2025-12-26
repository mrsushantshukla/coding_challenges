import argparse
import os
import sys

def count_bytes(filename):
    try:
        with open(file=filename, mode='rb') as f:
            f.seek(0, os.SEEK_END)
            byte_count = f.tell()
        return byte_count
    except Exception as e:
        print(f"Error counting bytes: {e}")
        return None

def count_lines(filename):
    try:
        with open(file=filename, mode='r', encoding='utf-8') as f:
            line_count = sum(1 for line in f)
        return line_count
    except Exception as e:
        print(f"Error counting lines: {e}")
        return None

def count_words(filename):
    try:
        with open(file=filename, mode='r', encoding='utf-8') as f:
            word_count = sum(len(line.split()) for line in f)
        return word_count
    except Exception as e:
        print(f"Error counting words: {e}")
        return None

def count_characters(filename):
    try:
        with open(file=filename, mode='r', encoding='utf-8') as f:
            char_count = sum(len(line) for line in f)
        return char_count
    except Exception as e:
        print(f"Error counting characters: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="CCWC: A Command-Line Tool")
    parser.add_argument("filename", help="Store filename")
    parser.add_argument("-c", "--count", help="Count bytes in the file", action="store_true", default=False)
    parser.add_argument("-l", "--lines", help="Count lines in the file", action="store_true", default=False)
    parser.add_argument("-w", "--words", help="Count words in the file", action="store_true", default=False)
    parser.add_argument("-m", help="Count characters in the file", action="store_true", default=False)
    args = parser.parse_args()
    
    if args.count:
        byte_count = count_bytes(args.filename)
        if byte_count is not None:
            print(byte_count, end=" ")
    if args.lines:
        line_count = count_lines(args.filename)
        if line_count is not None:
            print(line_count, end=" ")
    if args.words:
        word_count = count_words(args.filename)
        if word_count is not None:
            print(word_count, end=" ")
    if args.m:
        char_count = count_characters(args.filename)
        if char_count is not None:
            print(char_count, end=" ")
    if not (args.count or args.lines or args.words or args.m):
        byte_count = count_bytes(args.filename)
        if byte_count is not None:
            print(byte_count, end=" ")
        line_count = count_lines(args.filename)
        if line_count is not None:
            print(line_count, end=" ")
        word_count = count_words(args.filename)
        if word_count is not None:
            print(word_count, end=" ")
        char_count = count_characters(args.filename)
        if char_count is not None:
            print(char_count, end=" ")
    print(args.filename, end="\n")
if __name__ == "__main__":
    main()
    