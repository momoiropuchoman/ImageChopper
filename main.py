from PIL import Image

def get_image(file_name):
	return Image.open(file_name)

if __name__ == '__main__':

	# Please set the image path and the chopping size
	PATH = "Input the image path"
	CHOP_WIDTH = 32
	CHOP_HEIGHT = 32

	extension = PATH.split('.')[-1]

	image = get_image(PATH)

	image_width, image_height = image.size
	chop_num_x = image_width  // CHOP_WIDTH
	chop_num_y = image_height // CHOP_HEIGHT

	count = 1
	for i in range(chop_num_x):
		for j in range(chop_num_y):
			cropped_image = image.crop((CHOP_WIDTH*i, CHOP_HEIGHT*j, CHOP_WIDTH*i + CHOP_WIDTH, CHOP_HEIGHT*j + CHOP_HEIGHT))
			cropped_image.save(str(count) + '.' + extension)
			count += 1
