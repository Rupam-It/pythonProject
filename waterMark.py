# from  PIL   import Image ,ImageDraw,ImageFont

# img=Image.open('img.jpg')
# # img.show()



# text=input("Enter text for watermark: ")

# watermark=Image.new('RGBA',img.size,(161,91,70,0))

# font=ImageFont.truetype("arial",36)

# draw=ImageDraw.Draw(watermark)

# text_size=draw.textlength(text,font)

# center_x = (img.width - text_size[0]) / 2
# center_y = (img.height - text_size[1]) / 2


# draw.text((center_x, center_y), text, font=font, fill=(255,255,255,128))

# watermarked_image = Image.composite(watermark, img, watermark)

# watermarked_image.save("output_image.jpg")from PIL import Image, ImageDraw, ImageFont




from  PIL   import Image ,ImageDraw,ImageFont
# Open the image you want to watermark
img = Image.open('img.jpg')

# Define the text to be used as the watermark
text = input("Enter text for watermark: ")

# Create a new image for the watermark, with the same size as the original image
watermark = Image.new('RGBA', img.size, (161,91,70,0))

# Set the font to be used for the watermark
font = ImageFont.truetype('arial.ttf', 36)

# Create a drawing context for the watermark image
draw = ImageDraw.Draw(watermark)

# Get the size of the text, so that we can center it within the watermark image
text_size = draw.textsize(text, font=font)

# Calculate the coordinates of the center of the watermark image
center_x = int((img.width - text_size[0]) / 2)
center_y = int((img.height - text_size[1]) / 2)

# Draw the text onto the watermark image, centered within the image
draw.text((center_x, center_y), text, font=font, fill=(255, 255, 0, 128))

# Blend the watermark image with the original image, using an alpha mask
watermarked_img = Image.composite(watermark, img, watermark)

# Save the watermarked image to a file
watermarked_img.save('output_image.jpg')
