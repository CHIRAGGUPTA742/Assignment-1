def is_palindrome(n):
    
    new=word[::-1]
    if new==word:
        print("Yes, its a palindrome")
    else:
        print("No, its not a palindrome")
word=input()
is_palindrome(word)
