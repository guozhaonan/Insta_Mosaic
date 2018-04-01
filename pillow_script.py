from PIL import Image

#Access Image 1
im = Image.open('input_photos/test1.JPG')

#Access Image 3
im_three = Image.open('input_photos/test3.jpg')

#Start with Three Horizontal Pictures

def split_images(image):
    width = image.size[0]
    height = image.size[1]
    if height*3 < width: #3 Squares
        squaresize = (height, height)
        diff = (width - (height*3))/2
        threeleft = Image.new('RGB', squaresize)
        threemiddle =  Image.new('RGB', squaresize)
        threeright = Image.new('RGB', squaresize)
        crop_dimensions = []
        for position in range(0, 3):
            left = (position*height)+diff
            right = ((position+1)*height)+diff
            crop_dimensions.append((left, 0, right, height))
        threeleft.paste(image.crop(crop_dimensions[0]))
        threemiddle.paste(image.crop(crop_dimensions[1]))
        threeright.paste(image.crop(crop_dimensions[2]))
        threeleft.save('output_photos/left3.jpeg', 'jpeg')
        threemiddle.save('output_photos/middle3.jpeg', 'jpeg')
        threeright.save('output_photos/right3.jpeg', 'jpeg')
# elif height_three * 1.5 < width_three: #6 Squares
#     squaresize = (height_three/2, height_three/2)
#         diff =
split_images(im_three)
