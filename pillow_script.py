from PIL import Image

#Access Image
im = Image.open('test3.jpg')
width = im.size[0]
height = im.size[1]
#Start with Three Horizontal Pictures

if height*3 < width: #3 Squares
    squaresize = (height, height)
    diff = (width - (height*3))/2
    threeleft = Image.new('RGBA', squaresize)
    threemiddle =  Image.new('RGBA', squaresize)
    threeright = Image.new('RGBA', squaresize)
    crop_dimensions = []
    for position in range(0, 3):
        left = (position*height)+diff
        right = ((position+1)*height)+diff
        crop_dimensions.append((left, 0, right, height))
    threeleft.paste(im.crop(crop_dimensions[0]))
    threemiddle.paste(im.crop(crop_dimensions[1]))
    threeright.paste(im.crop(crop_dimensions[2]))
