# Zarnevis : RTL Text for your computer vision projects

## Installation 
### The `pip` way 

Just run this on your machine: 

```
pip install zarnevis
``` 

### The `git` way 

First, clone this repository using this command:

```
git clone https://github.com/prp-e/zarnevis
```

Then run these commands:

```
cd zarnevis && pip install -e . 
``` 

_NOTE_: This method is only suggested for when you're going to do some development and tests on the project. If you want to do something else (such as using this tool in a face tracker drone) just use the `pip` way and don't make trouble for yourself :) 

## Example 

It is pretty straight-forward. I actually made this because I wanted to do some cool stuff and I didn't want to make it so complex. This is an example code: 

```python
import cv2
from zarnevis import Zarnevis

image = cv2.imread('example.jpg')

processor = Zarnevis(image=image, text="اهواز زیبا", font_file='vazir.ttf', font_size=36, text_coords=(200,20), color=(255,0,100))
image = processor.draw_text()


cv2.imwrite('example_zarnevis.jpg', image)
``` 

### Image - Before 

![Example Image](example.jpg)

### Image - After 

![Example Image with Zarnevis](example_zarnevis.jpg)

## Special Thanks

- Amin Sharifi - Because he did a great job teaching this method on his [website](https://bigm.ir/persian-character-in-opencv/) and [YouTube channel](https://www.youtube.com/watch?v=RPb1X6Cf-ZU).
- Touhid Arastu - He pointed out in [this issue](https://github.com/prp-e/zarnevis/issues/1) that in new versions of Pillow, we don't really need reshaping and stuff and if we don't want to run our code on many different platforms, it can handle the thing itself. 