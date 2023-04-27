import pyscreenshot

def grab_specific_screen():
  pic = pyscreenshot.grab(bbox=(81, 135, 500, 300))
  pic.show()
  pic.save("ss.png")

def grab_whole_screen():
  "Grab the whole screen"
  import pyscreenshot as ImageGrab
  # grab fullscreen 
  im = ImageGrab.grab()
  # save image file
  im.show()
  im.save("fullscreen.png")

grab_whole_screen()