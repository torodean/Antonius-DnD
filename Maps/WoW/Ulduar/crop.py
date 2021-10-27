from PIL import Image

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()

num=4273
	
if __name__ == '__main__':
    for imgnumber in range(1,50):
        image = '{0}-{1}.jpg'.format(num,imgnumber)
        crop(image, (0, 0, 752, 506), 'cropped-{0}-{1}.jpg'.format(num,imgnumber))