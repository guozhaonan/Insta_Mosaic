from PIL import Image

# The following are test images, in order to make use of this for your own images, save your images to a variable like below

#Access Image 1
im_two = Image.open('input_photos/test2.JPG')

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
        up = []
        low = []
        for position in range(0, 3):
            left_zero = (position*six_square_size[0])+diff
            right_zero = ((position+1)*six_square_size[0])+diff
            up.append((left_zero, 0, right_zero, six_square_size[0]))
            low.append((left_zero, six_square_size[0], right_zero, six_square_size[0]*2))
        upper_left.paste(image.crop(up[0]))
        upper_middle.paste(image.crop(up[1]))
        upper_right.paste(image.crop(up[2]))
        lower_left.paste(image.crop(low[0]))
        lower_middle.paste(image.crop(low[1]))
        lower_right.paste(image.crop(low[2]))

        upper_left.save('output_photos/upleft.jpeg', 'jpeg')
        upper_middle.save('output_photos/upmiddle.jpeg', 'jpeg')
        upper_right.save('output_photos/upright.jpeg', 'jpeg')
        lower_left.save('output_photos/lowleft.jpeg', 'jpeg')
        lower_middle.save('output_photos/lowmiddle.jpeg', 'jpeg')
        lower_right.save('output_photos/lowright.jpeg', 'jpeg')
split_images(im_three, "three_squares")
