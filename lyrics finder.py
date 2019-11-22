import webbrowser

a = input("Search for lyrics: ")
L = list(a)
i = 0
while i < len(L):
    if L[i] == ' ':
        L[i] = '%20'
    i+= 1
searchTerm = ''.join(L)
webbrowser.open("https://genius.com/search?q="+searchTerm)