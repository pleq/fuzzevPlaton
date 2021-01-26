import requests

print('Input URL and path/to/wordlist with space between:')

while True:
    inps = input().split()
    if len(inps) != 2:
        print('Введите URL и путь/к/словарю через пробел!!!')
    else:
        break

baseurl, path = inps

def wordlist(path):
    with open(path,'r') as routes:
        allroutes = [row.strip() for row in routes if len(row) > 0 and row[0] != '#' and row != '\n']
    print(allroutes)
    return allroutes

allroutes = wordlist(path)

used = []

def findurl(url, listroutes):
    for route in listroutes:
        try:
            # if route not in used:
                r = requests.get(url + '/' + route)
                if r.status_code == 200:
                    # used.append(route)
                    print('We got `em! :' + url + '/' + route)
                    newrl = url + '/' + route
                    findurl(newrl, allroutes)
        except Exception as e:
            print('Something gone wrong oops!')
            print(e)

findurl(baseurl, allroutes)

print('Finalle')
# kinda path = 'lists/directory-list-1.0.txt'
