'''
# Average word length

Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

## Example

**Sample Input:**
this is some text

**Sample Output:**
3.5
'''

text = input("Introduce a text: ")
palabras = text.split()

totalLetras = len(text.replace(" ", ""))
totalPalabras = len(palabras)
print(round(totalLetras/totalPalabras, 1))
input()