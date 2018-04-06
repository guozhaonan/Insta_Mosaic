from PIL import Image

# The following are test images, in order to make use of this for your own images, save your images to a variable like below

#Access Image 1
im_one = Image.open('input_photos/test1.jpg')

#Access Image 2
im_two = Image.open('input_photos/test2.jpg')

#Access Image 3
im_three = Image.open('input_photos/test3.jpg')

#Access Image 4
im_four = Image.open('input_photos/test4.png')

im_five = Image.open('input_photos/test5.jpg')

#Start with Three Horizontal Pictures
def split_images(image, name):
    width = image.size[0]
    height = image.size[1]
    if height*3 <= width: #3 Squares
        three_square_size = (height, height)
        diff = (width - (height*3))/2
        image_array = [0,1,2]
        for position in range(0,3):
            image_array[position] = Image.new('RGB', three_square_size)
            left = (position*height)+diff
            right = ((position+1)*height)+diff
            image_array[position].paste(image.crop((left, 0, right, height)))
            image_array[position].save('output_photos/'+name+str(position)+'.jpeg', 'jpeg')
    elif height * 1.5 <= width: #6 Squares
        six_square_size = (height/2, height/2)
        diff = (width - (height*1.5))/2
        up = [0,1,2]
        low = [0,1,2]
        for position in range(0, 3):
            up[position] = Image.new('RGB', six_square_size)
            low[position] = Image.new('RGB', six_square_size)
            left = (position*six_square_size[0])+diff
            right = ((position+1)*six_square_size[0])+diff
            up[position].paste(image.crop((left, 0, right, six_square_size[0])))
            low[position].paste(image.crop((left, six_square_size[0], right, six_square_size[0]*2)))
            up[position].save('output_photos/'+name+str(position)+'.jpeg', 'jpeg')
            low[position].save('output_photos/'+name+str(position+3)+'.jpeg', 'jpeg')
    elif height == width:
        square_square = (height/3, width/3)
        up = [0,1,2]
        middle = [0,1,2]
        low = [0,1,2]
        for position in range(0, 3):
            up[position] = Image.new('RGB', square_square)
            middle[position] = Image.new('RGB', square_square)
            low[position] = Image.new('RGB', square_square)
            left = position*square_square[0]
            right = (position + 1)*square_square[0]
            up[position].paste(image.crop((left, 0, right, square_square[0])))
            middle[position].paste(image.crop((left, square_square[0], right, square_square[0]*2)))
            low[position].paste(image.crop((left, square_square[0]*2, right, square_square[0]*3)))
            up[position]
            middle[position].save('output_photos/'+name+str(position+3)+'.jpeg', 'jpeg')
            low[position].save('output_photos/'+name+str(position+6)+'.jpeg', 'jpeg')
    elif width < height:
        length = width//3
        horiz_diff = (width % 3)/2
        number_of_rows = height // length
        vertical_diff = (height % length)/2
        im_array=[[0 for x in range(number_of_rows)] for y in range(3)]
        for i in range(0,number_of_rows):
            for j in range(0,3):
                im_array[j][i] = Image.new('RGB', (length, length))
                left = (j*length)+horiz_diff
                right = ((j+1)*length)+horiz_diff
                up = (i*length)+vertical_diff
                down = ((i+1)*length)+vertical_diff
                im_array[j][i].paste(image.crop((left,up,right,down)))
                im_array[j][i].save('output_photos/'+name+str(j)+str(i)+'.jpeg', 'jpeg')
split_images(im_four, "var_squares")
