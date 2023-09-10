from PIL import Image

img = Image.open("images/soccer.gif")
print(img.size)

small_img = img.resize((20, 20))
small_img.save("images/soccer.gif")









