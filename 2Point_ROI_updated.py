def twopoint_roi():
    global image_path, image_name, image_format, twopt
    img = cv2.imread(image_path)
    roi = cv2.selectROI('step1>Click and Drag to select. step2>Hit Enter/Space to Save',img)
    
    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/2ptROI')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/2ptROI'
    new_dir.mkdir(parents=True, exist_ok=True)
    
    print(roi)
    img_cropped = img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
    img1=cv2.resize(img_cropped,(800,800))
    os.chdir(target)
    name = os.path.splitext(image_name)[0] + f'_{roi[0]}_{roi[1]}_{roi[2]}_{roi[3]}' + f'_2ptROI_{twopt}{image_format}'
    cv2.imwrite(name, img1)
    msgbox.showinfo(title='Info', message='2pt ROI image saved Successfully !')
    cv2.destroyWindow('step1>Click and Drag to select. step2>Hit Enter/Space to Save')
    twopt += 1
