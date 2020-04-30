# Photo Splitter

A few lines of code, written in Python 3, using the `PIL` library to split an image in `n` sub-images.

It was built to split panoramic pictures to post them on instagram.... hehehe. 

## Here's an example

### Original picture:

![Full Image](https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/readme_imgs/i_love_you_so_much.jpg "Full")

### Splits:
<div>
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/readme_imgs/0.jpg" height="350">
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/readme_imgs/1.jpg" height="350">
<img src="https://raw.githubusercontent.com/joseluishaddad/PyThings/master/photo_split/readme_imgs/2.jpg" height="350">
</div>

So go check them out [here](https://www.instagram.com/josehaddadc) if you feel like doing so :wink:


# Splitter Telegram Bot
Yes! It could be a pain in the *** to run the code every time you want to split a picture, so i created a telegram that does it for you and then deletes the files.

## How it Works?
1. Receives an image under 20MB
2. Receives the command `/split <n> <axis>` with the parameters for the split.
3. Returns the splitted image.

NOTE: It's not yet deployed, but will be anytime soon.
