import sys 

sys.path.append("..")
import main
from PIL import Image, ImageDraw, ImageFont

def break_fix(text, width, font, draw):
    if not text:
        return
    lo = 0
    hi = len(text)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        t = text[:mid]
        w, h = draw.textsize(t, font=font)
        if w <= width:
            lo = mid
        else:
            hi = mid - 1
    t = text[:lo]
    w, h = draw.textsize(t, font=font)
    yield t, w, h
    yield from break_fix(text[lo:], width, font, draw)

#uses binary search to find space strings in order to fit the image 
#automatically left aligns the text
def fit_text(img, text, color, font):
    width = 400
    draw = ImageDraw.Draw(img)
    pieces = list(break_fix(text, width, font, draw))
    height = sum(p[2] for p in pieces)
    if height > img.size[1]:
        raise ValueError("error, doesn't fit")
    y = (img.size[1] - height) // 2
    for t, w, h in pieces:
        x = 30
        draw.text((x, y), t, font=font, fill=color)
        y += h

#actual video is going to be 1080x1920 (vertical videos e.g. YT shorts, Instagram reels, Tiktok)
width = 500
height = 300
font = ImageFont.truetype("verdana.ttf", size=15)

for i in range(len(main.comments)):
    img = Image.new('RGB', (width, height), color=(26, 26, 27))
    imgDraw = ImageDraw.Draw(img)

    fit_text(img, main.authors[i] + main.comments[i], (255, 255, 255), font=font)
    img.save(str(i) + ".png")