Photo Splitter for Mosaic-like Instagram Profiles
=================================================

This is a script to split up photos to turn Instagram accounts into landing pages. An example of a site that already does this is [Jaden Smith's account](https://www.instagram.com/c.syresmith/?hl=en)

# Dependencies

* [Pillow](https://pillow.readthedocs.io/en/latest/)

# Usage

### Images must fit one of the following criteria:

* height is less than one-third the width in pixels, these are very long images(creates 3 images)
* height is less than the width * 1.5 in pixels (creates 6 images)

If they fit these criteria, first put your photo into the input_photos folder.

### Assign variables to your photos:

```python
im = Image.open('input_photos/photo_name')
```

### Run the method at the bottom of the script:

```python
split_images(im)
```

# Sample Output
![Screenshot from My Phone](https://github.com/guozhaonan/insta_landing/blob/master/md_images/screenshot.jpg)


# To Do:

* Web App Functionality (current thoughts are Flask, Django, or Pyramid)
* Adding in Blank Photos
* Adding in 3x3 Functionality
* Adding in the ability to write words into photos
* Adding in the ability to post directly to Instagra
