Photo Splitter for Mosaic-like Instagram Profiles
=================================================

This is a script to split up photos to turn Instagram accounts into landing pages. An example of a site that already does this is [Jaden Smith's account](https://www.instagram.com/c.syresmith/?hl=en)

# Dependencies

* [Pillow](https://pillow.readthedocs.io/en/latest/)

# Usage

### Images must fit one of the following criteria:

* height is less than one-third the width in pixels, these are very long images(creates 3 images)
* height is less than the width * 1.5 in pixels (creates 6 images)
* height is the same as the width (creates 9 images)

If they fit these criteria, first put your photo into the input_photos folder.

### Assign variables to your photos:

```python
im = Image.open('input_photos/photo_name')
```

### Run the method at the bottom of the script:

```python
split_images(im, 'image_name_base')
```

# Sample Output

### Demonstration of 3 squares and 6 squares
![Screenshot from My Phone](https://github.com/guozhaonan/insta_landing/blob/master/md_images/screenshot1.jpg)

### Demonstration of 9 squares

![Screenshot from My Phone](https://github.com/guozhaonan/insta_landing/blob/master/md_images/screenshot2.jpg)

# To Do:

* Web App Functionality (current thoughts are Flask, Django, or Pyramid)
* Allowing Photo-Stitching
* Adding in the ability to write words into photos
* Adding in the ability to post directly to Instagram
