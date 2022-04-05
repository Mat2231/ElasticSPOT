import requests, json, re
global url

# Actual url


print('''
╔═╗┬  ┌─┐┌─┐┌┬┐┬┌─┐╔╦╗╔╗       ╔═╗┌─┐┌─┐┬─┐┌─┐┬ ┬
║╣ │  ├─┤└─┐ │ ││───║║╠╩╗      ╚═╗├┤ ├─┤├┬┘│  ├─┤
╚═╝┴─┘┴ ┴└─┘ ┴ ┴└─┘═╩╝╚═╝      ╚═╝└─┘┴ ┴┴└─└─┘┴ ┴

''')


timeout_seconds=int(input("[#] Enter request timeout time in seconds ex(5) : " ))
print('\n')

def main_part():
    url = '/'+urll+'/'



    r = requests.get('http:/'+url+url1, timeout=timeout_seconds)

    x3 = ((((r.text.split("\n",1)[1]).replace("green  open   ", "")).replace("yellow open   ", "")).replace("red  open   ", ""))


    # print("\n\n"+x3+"\n\n")

    file1 = open("ignore.txt", "a")
    file1.write(x3)
    file1.close()

    def clean_file(file):
        f = open(file, 'r+')
        f.truncate(0) # need '0' when using r+# same thing as last but now into another files
    # But filtered index list into text file so it can be worked with
    with open('ignore.txt', 'r') as bruh:
        lines = bruh.readlines()

    # Clear ingore.txt
    clean_file("ignore.txt")



    with open('ignore.txt', 'a') as fout:
        for line in lines:
            # Remove lines that start with api and /.
            if not line.strip().startswith(("api",".")):
                fout.write(line)
            # if not line.strip().startswith((".")):
            #     fout.write(line
    bruh = open("ignore.txt").read()
    sep = ' '
    print(bruh+"\n\n")


    with open('ignore.txt') as f:
        servers = [line.rstrip() for line in f]
        f.close()
    clean_file("ignore.txt")

    index_list=[]


    # This will use the index's put into a list and search each one of them for the keyword string
    def search_index():
        global index1

        index_list=(servers[a]).split(sep, 1)[0]

        # print(index_list)
        url2=('http:/'+url+index_list+"/_search?pretty=true&size=25")
        print("                 "+"[!]  Searching    -   "+url2+'\n\n')


        r = requests.get(url2, timeout=timeout_seconds)
        text=r.text
        if "json" in str(r.headers):
            if case_sensitive == True:
                if keyword in text:
                    print("\n\nFOUND!!!\n\n")
                    file1 = open("Saved.txt", "a")
                    file1.write(url2+"  "+keyword+'\n')
                    file1.close()
            if case_sensitive == False:
                if(keyword.upper() in text.upper()):
                         print("\n\nFOUND!!!\n\n")
                         file1 = open("Saved.txt", "a")
                         file1.write(url2+"  "+keyword+'\n')
                         file1.close()

                else:
                    pass
        else:
            print('\n[!] NOT ELASTIC! Skiping\n')
            pass
        # print(r.text)

        file1 = open("ignore.txt", "a")
        file1.write(index_list+'\n')
        file1.close()


    for a in range(1000):
        #

        # Goes through each index name and makes requests with it that will be used for searching
        try:
            search_index()
        except:
            pass


    bruh = open("ignore.txt").read()
    with open('ignore.txt') as f:
        IndexListInAcualList = [line.rstrip() for line in f]
    # print(index1)
    # print(bruh)
    # print(IndexListInAcualList[3])


    clean_file("ignore.txt")
    file1 = open("Saved.txt", "a")
    file1.write('\n')


# Url to list indexes

url1=('_cat/indices?v')
while True:
    type=input('[1] Enter custom IP\n[2] Iterate through file\n\n[1/2]: ')
    if type == '1':
        global urll
        urll=input("\n[-] Enter IP Ex:(0.00.47.62:9200) : ")
        print('\n')
        # time = input('[#] How many seconds until timeout? :')
        while True:
            case=input('[y/n] Case sensitive? : ')
            if case == 'y':
                case_sensitive=True
                break
            if case == 'n':
                case_sensitive=False
                break
        print('\n')
        keyword=input('\n[?]  Enter keyword to search for: ')
        print('\n')
        main_part()
        break
    if type == '2':
        # Ask if case sensitive, then ask for keyword to search for, then open Servers.txt as list
        # time = input('[#] How many seconds until timeout? :')
        while True:
            case=input('\n[y/n] Case sensitive? : ')
            if case == 'y':
                case_sensitive=True
                break
            if case == 'n':
                case_sensitive=False
                break


        # Open Server.txt and put it into list
        keyword=input('[?]  Enter keyword to search for: ')
        print('\n')

        with open('Servers.txt') as f:
            servers = [line.rstrip() for line in f]


        # Go through each url and run the main script using the url we got from Servers.txt
        for idx, word in enumerate(servers):
            print('Searching '+word+"!")
            urll=word
            try:
                main_part()
                # If it takes to long it will skip it
            except:
                pass
        break
