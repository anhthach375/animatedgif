from PIL import Image, ImageOps
import math # This code calculates the log with base 2 using the math function log: math.log(_____,2). 
# ignore_missing_imports = True

def flappingToaster() -> None:
    """ Loads 4 flying toaster images from file and 
    creates/saves an animated gif with the images as frames. """

    # each frame will be accumulated into a list
    toasterFrames:list = []

    # the files are named with the pattern toasterNUM.gif, as in:
    #   toaster0.gif, toaster1.gif, toaster2.gif, toaster3.gif
    # this pattern means we can iterate over the values 0,1,2,3
    for i in range(4):
        # for this frame, figure out the corresponding file name
        # since the images are within the folder "toasters", we 
        # put "toasters/" at the beginning to tell Python where to look
        toasterFileName:str = "toasters/toaster" + str(i) + ".gif"

        # load the single image file
        toasterImage:Image = Image.open( toasterFileName )

        # accumulate this frame into the list
        toasterFrames.append(toasterImage)
    
    # ask the first frame to create and save an animated gif
    # the optional parameter append_images is assigned a list with additional frames
    toasterFrames[0].save('animations/flappingToaster.gif', save_all=True, 
                            append_images=toasterFrames[1:], 
                            duration=80, loop=0)

def slideTheGates(numFrames:int) -> None:
    """ Opens an image of the MHC gates and animates a sweep
    reveal effect across numFrames steps. Saves the file to animations/slidingGates.gif """

    # load the gates image
    gates:Image = Image.open( "nightGates.jpg" )

    # each frame will be accumulated into a list
    gateFrames:list = []

    # how much to reveal each frame
    revealIncrement:int = gates.width//(numFrames-1)

    # accumulate how much is revealed each time
    revealedWidth:int = 0 # initialize to 0

    # for each frame
    for i in range(numFrames):
        # create a blank background
        background:Image = Image.new('RGB', (gates.width, gates.height), "black")

        # extract a portion of the gates using the crop method
        currentGate:Image = gates.crop((0,0,revealedWidth,gates.height))

        # put the extrated portion onto the background
        background.paste(currentGate)

        # add the frame 
        gateFrames.append( background )

        # update how much to reveal the next iteration
        revealedWidth += revealIncrement

    # ask the first frame to create and save an animated gif
    # the optional parameter append_images is assigned a list with additional frames
    # the optional parameter duration is set to 200 (ms) for how long each frame shows
    gateFrames[0].save("animations/slidingGates.gif",
        save_all=True, append_images=gateFrames[1:], duration=200, loop=0)

def openTheGates(numFrames:int) -> None:
    """ Opens an image of the MHC gates and animates a sweep colorization
    effect across numFrames steps. Saves the file to animations/openingGates.gif """

    # load another gates image
    gates:Image = Image.open( "uncommonWomenMHC.png" )

    # convert it to grayscale and back to RGBA so the format is consistent
    grayGates:Image = ImageOps.grayscale(gates).convert('RGBA')

    # each frame will be accumulated into a list
    gateFrames:list = []

    # for each frame
    for i in range(numFrames):
        # create a copy of the background for this frame
        currentFrame:Image = grayGates.copy()

        # we want to reveal only part of the color version
        # let's evenly distribute how much we reveal each time
        revealedWidth:int = i*gates.width//(numFrames-1)

        # extract a portion of the (full color) gates using the crop method
        currentGate:Image = gates.crop((0,0,revealedWidth,gates.height))

        # paste the cropped image onto the gray background
        currentFrame.paste(currentGate)

        # add the frame 
        gateFrames.append( currentFrame )

    # ask the first frame to create and save an animated gif
    # the optional parameter append_images is assigned a list with additional frames
    gateFrames[0].save("animations/openingGates.gif",
        save_all=True, append_images=gateFrames[1:], duration=160, loop=0)

def dragonOnGate( xLocation:int ) -> None:
    """ Opens an image of the MHC gates and an image of a dragon.
    Pastes the dragon onto the gates image at the specified xLocation. 
    Saves the file to dragonGate.png """

    # load a gates image
    gates:Image = Image.open( "nightGates.jpg" )

    # load the dragon
    dragon:Image = Image.open( "dragon.png" )

    # paste the dragon onto the background
    gates.paste(dragon, (xLocation, 0), dragon)

    # save the image
    gates.save( "dragonGate.png" )

def dragons() -> None:
# You'll notice there is a folder in your workspace called dragons. This contains 25 dragon images 
    animationFrames:list = []
    # the files are named with the pattern dragon_Num.png, as in: dragon_0.png, dragon_1.png
    # this pattern means we can iterate over the values 0,1,2,3
    for i in range(25):
        # for this frame, figure out the corresponding file name
        # since the images are within the folder "dragons", we 
        # put "dragons/" at the beginning to tell Python where to look
        animationsFileName:str = "dragons/dragon_" + str(i) + ".png"

        # load the single image file
        animationImage:Image = Image.open(animationsFileName )

        # accumulate this frame into the list
        animationFrames.append(animationImage)
    animationFrames[0].save('animations/animatedDragon.gif', save_all=True, 
                            append_images=animationFrames[:20], 
                            duration=80, loop=0)

def openTheGatesExp() -> None:
 # load another gates image
    gates:Image = Image.open( "uncommonWomenMHC.png" )

    # convert it to grayscale and back to RGBA so the format is consistent
    grayGates:Image = ImageOps.grayscale(gates).convert('RGBA')

    numFrames: int = int(math.ceil(math. log(gates.width, 2) )) + 1

    # each frame will be accumulated into a list
    gateFrames:list = []

    for i in range(numFrames):
        # create a copy of the background for this frame
        currentFrame:Image = grayGates.copy()

        # we want to reveal only part of the color version
        # let's evenly distribute how much we reveal each time
        revealedWidth:int = 2**i

        # extract a portion of the (full color) gates using the crop method
        currentGate:Image = gates.crop((0,0,revealedWidth,gates.height))

        # paste the cropped image onto the gray background
        currentFrame.paste(currentGate)

        # add the frame 
        gateFrames.append( currentFrame )

    # ask the first frame to create and save an animated gif
    # the optional parameter append_images is assigned a list with additional frames
    gateFrames[0].save("animations/openingGatesExp.gif",
        save_all=True, append_images=gateFrames[1:], duration=300, loop=0)

def dragonGates(numFrames:int) -> None:
# load another gates image
# https://janicehayescha.com/shop/uncommon-women-mount-holyoke-college/
    gates: Image = Image.open("uncommonWomenMHC.png")
# load the dragon
    dragon: Image = Image.open( "dragon.png" )
# each frame will be accumulated into a list
    gateFrames: list = []
# for each frame
    for i in range(numFrames):
# create a copy of the background for this frame
        currentFrame: Image = gates.copy()
# we want to the dragon to move each frame
        xLocation: int = i*gates.width//(numFrames-2)
# paste the dragon onto the background
        currentFrame.paste(dragon, (xLocation, 0), dragon)
# add the frame
        gateFrames.append (currentFrame)
# ask the first frame to create and save an animated gif
    gateFrames [0] .save ("animations/dragonGates.gif",
        save_all=True, append_images=gateFrames [1:], duration=160, loop=0)


def main():
    # dragonGates(20)
    openTheGatesExp()
    dragonGates(20)

# def test():

if __name__ == "__main__":
    main()
    # test()
