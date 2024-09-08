def onepoint_roi():
    global image_path, image_name, image_format, onept
    
    img = cv2.imread(image_path, 1)
 
    cv2.imshow('image', img)
 
    cv2.setMouseCallback('image', click_event)
 
    cv2.waitKey(0)
    
def click_event(event, x, y, flags, params):
    global opened_image, image_path, image_height, image_width, image_name, image_format, onept
 
    if event == cv2.EVENT_LBUTTONDOWN:

        img = Image.open(image_path)

        new_path = tk_file.askdirectory()
        new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/1ptROI')
        target = new_path + '/' + os.path.splitext(image_name)[0] + '/1ptROI/' + os.path.splitext(image_name)[0] + '_1ptROI'
        new_dir.mkdir(parents=True, exist_ok=True)
        
        x1 = x-400 if (x-400) >= 0 else 0
        y1 = y-400 if (y-400) >= 0 else 0
        x2 = x+400 if (x+400) <= image_width else image_width
        y2 = y+400 if (y+400) <= image_height else image_height

        cord = (x1, y1, x2, y2)
        print('%s %s' % (image_path, cord))
        img.crop(cord).save(f'%s-x%03d-y%03d1ptROI{onept}{image_format}' % (target, image_width, image_height / 2))

        msgbox.showinfo(title='Info', message='One image saved successfully !')
        cv2.destroyWindow('image')
        onept += 1