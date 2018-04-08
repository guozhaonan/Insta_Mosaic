from PIL import Image
#Start with Three Horizontal Pictures
#if the an output photo is in the following aspect 'output_photos/photo.png', output_photo_path should be similar to 'output_photos/', same goes for image_path
def split_images(image_path, name, output_photo_path):
    image = Image.open(image_path)
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
            image_array[position].save(output_photo_path+name+str(position)+'.jpeg', 'jpeg')
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
            up[position].save(output_photo_path+name+str(position)+'.jpeg', 'jpeg')
            low[position].save(output_photo_path+name+str(position+3)+'.jpeg', 'jpeg')
    elif width <= height:
        #Calculate the Length of the Square
        length = width//3
        #Calculate the amount of space left over on either side horizontally
        horiz_diff = (width % 3)/2
        #Calculate the amount of rows
        number_of_rows = height // length
        #Calculate the amount of space left over on either side vertically
        vertical_diff = (height % length)/2
        #Create a temporary array of numbers that will be replaced with photo objects
        im_array=[[0 for x in range(number_of_rows)] for y in range(3)]
        #Looping through the array to make the individual images, past the parts cropped from the original image, and save them to a folder
        for i in range(0,number_of_rows):
            for j in range(0,3):
                im_array[j][i] = Image.new('RGB', (length, length))
                left = (j*length)+horiz_diff
                right = ((j+1)*length)+horiz_diff
                up = (i*length)+vertical_diff
                down = ((i+1)*length)+vertical_diff
                im_array[j][i].paste(image.crop((left,up,right,down)))
                im_array[j][i].save(output_photo_path+name+str(j)+str(i)+'.jpeg', 'jpeg')

split_images('input_photos/test3.jpg', 'dolo', 'output_photos/')
