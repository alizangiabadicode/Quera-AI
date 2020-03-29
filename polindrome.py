import sys
lines = sys.stdin.readlines()
temp = ''.join(filter(lambda x: ord('a')<=ord(x)<=ord('z') or ord('A')<=ord(x)<=ord('Z') or x == ' ', ''.join(lines)))
input = temp.split(' ')
polindrome_words = []
def is_polindrome(word):
    if word.lower() == word[::-1].lower() and word != '':
        return True
    else:
        return False
for word in input:
    if is_polindrome(word):
        polindrome_words.append(word)
if len(polindrome_words) == 0:
    print("No palindrome words found :(")
else:
    print("Palindrome words in the text are: ", ', '.join(polindrome_words))
