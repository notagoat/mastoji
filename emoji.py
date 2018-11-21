import requests
import urllib.request
import os.path
import shutil
import csv

def main():
    with open("instances.txt") as i:
        instances = i.readlines()
    instances = [x.strip() for x in instances]

    instances.sort()
    setup(instances)
    clone(instances)
    try:
        for name in instances:
            print("-----!"+name+"!-----")
            fetch(name)
    except Exception as e:
        print("Instance Error")
        print(e)


def fetch(name):
    r = requests.get('https://%s/api/v1/custom_emojis'% name, allow_redirects=True)
    path = "emoji/%s/" % name
    try: 
        for emoji in r.json():
            try:
                if os.path.isfile(path+emoji['shortcode']+".png"):
                    pass
                else:
                    print(emoji['shortcode'] + " found!")
                    emojiimage = requests.get(emoji['static_url'],allow_redirects=True)
                    open(path + emoji['shortcode']+".png",'wb').write(emojiimage.content)
            except Exception as e:
                print("Did not get: " + emoji['url'])
                print(e)
                pass
    except Exception as e:
        print(e)

def setup(instances): 
    if (os.path.isdir("emoji/")):
        pass   
    else:
        os.mkdir("emoji/")

    for name in instances:
        if (os.path.isdir("emoji/%s/"%name)):
            pass
        else: os.mkdir("emoji/%s/"%name)
 
    if (os.path.isdir("emoji/all")):
        pass
    else:
        os.mkdir("emoji/all")

def clone(instances):
    for name in instances:
        print("Copying emoji for: %s"% name)
        path = "emoji/%s/" % name
        files = os.listdir(path)
        for name in files:
            try:
                shutil.copyfile(path+name,"emoji/all/"+name)
            except Exception as e:
                print(e)
                pass
 

if __name__ == '__main__':
    main()