from PIL import Image, ImageDraw, ImageFont


def write_text_on_image():
	'''
	write texts over a given position of the given image.
	'''
	with Image.open("0000/profile.png") as im:
		try:
			weight, height = im.size
			base = ImageDraw.Draw(im)
			text_font = ImageFont.truetype("Arial.ttf", 100)
			base.text((8 / 10 * weight, 1 / 10 * height), '3', fill=(0, 0, 255), font=text_font)
			im.save('0000/output.png')
		except IOError:
			pass


write_text_on_image()
