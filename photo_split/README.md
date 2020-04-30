# Photo Splitter

A few lines of code, written in Python 3, using the `PIL` library to split an image in `n` sub-images.

It was built to split panoramic pictures to post them on instagram.... hehehe. 

## Here's an example

### Original picture:

![Full Image](https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/input/usain_jose.jpg "Full")

### Splits:
<div>
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/output/img0.jpg" height="400">
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/output/img1.jpg" height="400">
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/output/img2.jpg" height="400">
</div>

So go check them out [here](https://www.instagram.com/josehaddadc) if you feel like doing so :wink:


# Splitter Telegram Bot
## How it Works?
1. Receives an image under 20MB
2. Receives the command `/splits <n> <axis>` with the parameters for the split.
3. Returns the splitted image.