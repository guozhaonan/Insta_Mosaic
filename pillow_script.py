from PIL import Image

#Access Image
im = Image.open('input_photos/test3.jpg')
width = im.size[0]
height = im.size[1]
#Start with Three Horizontal Pictures

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
    threeleft.paste(im.crop(crop_dimensions[0]))
    threemiddle.paste(im.crop(crop_dimensions[1]))
    threeright.paste(im.crop(crop_dimensions[2]))
    threeleft.save('output_photos/left3.jpeg', 'jpeg')
    threemiddle.save('output_photos/middle3.jpeg', 'jpeg')
    threeright.save('output_photos/right3.jpeg', 'jpeg')
