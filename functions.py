import requests
import webbrowser
import os
import time
from PIL import Image


def head():

    nick = input("Nickname: ")

    if os.path.exists("agent.txt"):
        pass
    else:
        webbrowser.open('https://www.whatsmyua.info/', new=2)
        agent = input(
            "Your User-Agent(Your default browser will open now, you should copy your User-Agent. After, insert it here. We don't steal your data!)")

        file = open("agent.txt", "wb")
        file.write(agent)
        file.close()

    with open("agent.txt", "r") as txt:
        headers = {
            'User-Agent': f'{txt}'
        }
        print(headers)

    url = f"https://tlauncher.org/upload/all/nickname/{nick}.png"

    name = url.split("/")
    name = name[len(name)-1]

    print(f"Skin will be saved as {name} in {os.getcwd()}")

    if os.path.exists(name):
        os.remove(name)

    try:
        response = requests.get(url, headers=headers)
        file = open(f"{nick}.png", "wb")
        file.write(response.content)
        file.close()
    except:
        print(f"Nickname {nick} not found")
        print("")
        time.sleep(1)

    im = Image.open(name)

    im_crop1 = im.crop((8, 8, 16, 16))
    im_crop2 = im.crop((40, 8, 48, 16))
    im_crop2.save("crop2.png")
    print(f"Head will be saved as 'head-{name}' in {os.getcwd()}")
    mask_im = Image.open('crop2.png').resize(im_crop1.size).convert('RGBA')
    im_crop1.paste(im_crop2, mask_im)
    im_crop1.save(f'head-{name}')

    os.remove("crop2.png")
    os.remove(name)


def skin():
    nick = input("Nickname: ")

    if os.path.exists("agent.txt"):
        pass
    else:
        webbrowser.open('https://www.whatsmyua.info/', new=2)
        agent = input(
            "Your User-Agent (Your default browser will open now, you should copy your User-Agent. After, insert it here. We don't steal your data!): ")

        file = open("agent.txt", "wb")
        file.write(agent.encode("utf-8"))
        file.close()

    with open("agent.txt", "r") as txt:
        headers = {
            'User-Agent': f'{txt}'
        }
        print(headers)

    url = f"https://tlauncher.org/upload/all/nickname/tlauncher_{nick}.png"
    name = url.split("/")
    name = name[len(name)-1]

    print(f"Skin will be saved as {name}")

    if os.path.exists(name):
        os.remove(name)

    try:
        response = requests.get(url, headers=headers)
        file = open(f"{nick}.png", "wb")
        file.write(response.content)
        file.close()
    except:
        print(f"Nickname {nick} not found")
        print("")
        time.sleep(1)