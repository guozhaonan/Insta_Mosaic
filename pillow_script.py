from PIL import Image

# The following are test images, in order to make use of this for your own images, save your images to a variable like below

#Access Image 1
im_one = Image.open('input_photos/test1.jpg')

#Access Image 2
im_two = Image.open('input_photos/test2.jpg')

#Access Image 3
im_three = Image.open('input_photos/test3.jpg')

#Start with Three Horizontal Pictures

def split_images(image, name):
    width = image.size[0]
    height = image.size[1]
    if height*3 <= width: #3 Squares
        three_square_size = (height, height)
        diff = (width - (height*3))/2
        threeleft = Image.new('RGB', three_square_size)
        threemiddle =  Image.new('RGB', three_square_size)
        threeright = Image.new('RGB', three_square_size)
        image_array = [threeleft, threemiddle, threeright]
        for position in range(0, 3):
            left = (position*height)+diff
            right = ((position+1)*height)+diff
            image_array[position].paste(image.crop((left, 0, right, height)))
            image_array[position].save('output_photos/'+name+str(position)+'.jpeg', 'jpeg')
    elif height * 1.5 <= width: #6 Squares
        six_square_size = (height/2, height/2)
        diff = (width - (height*1.5))/2
        upper_left = Image.new('RGB', six_square_size)
        upper_middle = Image.new('RGB', six_square_size)
        upper_right = Image.new('RGB', six_square_size)
        lower_left = Image.new('RGB', six_square_size)
        lower_middle = Image.new('RGB', six_square_size)
        lower_right = Image.new('RGB', six_square_size)
        up = [upper_left, upper_middle, upper_right]
        low = [lower_left, lower_middle, lower_right]
        for position in range(0, 3):
            left = (position*six_square_size[0])+diff
            right = ((position+1)*six_square_size[0])+diff
            up[position].paste(image.crop((left, 0, right, six_square_size[0])))
            low[position].paste(image.crop((left, six_square_size[0], right, six_square_size[0]*2)))
            up[position].save('output_photos/'+name+str(position)+'.jpeg', 'jpeg')
            low[position].save('output_photos/'+name+str(position+3)+'.jpeg', 'jpeg')
    elif height == width:
        square_square = (height/3, width/3)
        upper_left = Image.new('RGB', square_square)
        upper_middle = Image.new('RGB', square_square)
        upper_right = Image.new('RGB', square_square)
        middle_left = Image.new('RGB', square_square)
        middle_middle = Image.new('RGB', square_square)
        middle_right = Image.new('RGB', square_square)
        lower_left = Image.new('RGB', square_square)
        lower_middle = Image.new('RGB', square_square)
        lower_right = Image.new('RGB', square_square)
        up = [upper_left, upper_middle, upper_right]
        middle =[middle_left, middle_middle, middle_right]
        low = [lower_left, lower_middle, lower_right]
        for position in range(0, 3):
            left = position*square_square[0]
            right = (position + 1)*square_square[0]
            up[position].paste(image.crop((left, 0, right, square_square[0])))
            middle[position].paste(image.crop((left, square_square[0], right, square_square[0]*2)))
            low[position].paste(image.crop((left, square_square[0]*2, right, square_square[0]*3)))
            up[position].save('output_photos/'+name+str(position)+'.jpeg', 'jpeg')
            middle[position].save('output_photos/'+name+str(position+3)+'.jpeg', 'jpeg')
            low[position].save('output_photos/'+name+str(position+6)+'.jpeg', 'jpeg')
split_images(im_one, "square_squares")
