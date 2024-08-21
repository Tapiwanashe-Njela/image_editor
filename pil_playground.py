from PIL import Image, ImageFilter, ImageEnhance

    # - Image -
with Image.open("Baby.jpg") as picture:
    #picture.show() #To show the picture on the screen

    black_white = picture.convert("L") #always takes L as argument
    black_white.save("b_w_Baby.jpg")
    #black_white.show() #show on screen

    mirrored = picture.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored.save("mirrored_Baby.jpg") #always save with the same .ext
    #mirrored.show()

    # - ImageFilter -
    blur = picture.filter(ImageFilter.BLUR)
    #blur.show()

    # - ImageEnhance -
    contrast = ImageEnhance.Contrast(picture)
    contrast = contrast.enhance(1.6) #all start from 1 = 100%, 1.2 is 120% etc
    contrast.save("contrast_Baby.jpg")
    #contrast.show()

    #faster way
    color = ImageEnhance.Color(picture).enhance(1.8)
    color.save("colored_Baby.jpg")
    #color.show()

    
    
    
    

    