import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.filedialog as tk_file
from PIL import Image, ImageTk
import pathlib
import os
import cv2


screen = tk.Tk()
screen.title('Medical Image Tool')
screen.geometry('800x600')
#screen.iconbitmap('C:/Users/praky/OneDrive - Manipal Academy of Higher Education/Mini Project Develop Tool for Medical Images/gui/Final/manipal.ico')
screen.config(bg='black')

edited_image = ''
opened_image = ''
image_path = ''
image_name = ''
image_format = ''
image_height = 0
image_width = 0
onept = 1
twopt = 1

def h_slice():
    global opened_image, image_path, image_height, image_width, image_name, image_format
    img = Image.open(image_path)

    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/H Slice')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/H Slice/' + os.path.splitext(image_name)[0] + '_H_slice'
    new_dir.mkdir(parents=True, exist_ok=True)

    cord = (0, 0, image_width, image_height / 2)
    print('%s %s' % (image_path, cord))
    img.crop(cord).save(f'%s-x%03d-y%03dTOP{image_format}' % (target, image_width, image_height / 2))

    cord = (0, image_height / 2, image_width, image_height)
    print('%s %s' % (image_path, cord))
    img.crop(cord).save(f'%s-x%03d-y%03dBOTTOM{image_format}' % (target, image_width, image_height / 2))

    msgbox.showinfo(title='Info', message='Two images saved successfully !')


def v_slice():
    global opened_image, image_path, image_height, image_width, image_name, image_format
    img = Image.open(image_path)

    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/V Slice')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/V Slice/' + os.path.splitext(image_name)[0] + '_V_Slice'
    new_dir.mkdir(parents=True, exist_ok=True)

    cord = (0, 0, image_width / 2, image_height)
    print('%s %s' % (image_path, cord))
    img.crop(cord).save(f'%s-x%03d-y%03dLEFT{image_format}' % (target, image_width / 2, image_height))

    cord = (image_width / 2, 0, image_width, image_height)
    print('%s %s' % (image_path, cord))
    img.crop(cord).save(f'%s-x%03d-y%03dRIGHT{image_format}' % (target, image_width / 2, image_height))

    msgbox.showinfo(title='Info', message='Two images saved successfully !')


def grid_slicer2():
    global opened_image, image_path, image_height, image_width, image_name, image_format
    h_cut = int(image_height / 2)
    w_cut = int(image_width / 2)

    img = Image.open(image_path)

    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/2x2')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/2x2/' + os.path.splitext(image_name)[0] + '_2x2'
    new_dir.mkdir(parents=True, exist_ok=True)

    for x0 in range(0, image_width, w_cut):
        for y0 in range(0, image_height, h_cut):
            cord = (x0, y0,
                    x0 + w_cut if x0 + w_cut < image_width else image_width - 1,
                    y0 + h_cut if y0 + h_cut < image_height else image_height - 1)
            print('%s %s' % (image_path, cord))

            if ((x0 + w_cut) - x0) > 5 and ((y0 + h_cut) - y0) > 5:
                img.crop(cord).save(f'%s-x%03d-y%03d{image_format}' % (target, x0, y0))

    msgbox.showinfo(title='Info', message='Four images saved successfully !')


def grid_slicer4():
    global opened_image, image_path, image_height, image_width, image_name, image_format
    h_cut = int(image_height / 4)
    w_cut = int(image_width / 4)

    img = Image.open(image_path)

    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/4x4')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/4x4/' + os.path.splitext(image_name)[0] + '_4x4'
    new_dir.mkdir(parents=True, exist_ok=True)

    for x0 in range(0, image_width, w_cut):
        for y0 in range(0, image_height, h_cut):
            cord = (x0, y0,
                    x0 + w_cut if x0 + w_cut < image_width else image_width - 1,
                    y0 + h_cut if y0 + h_cut < image_height else image_height - 1)
            print('%s %s' % (image_path, cord))

            if (image_width - x0) > 5 and (image_height - y0) > 5:
                img.crop(cord).save(f'%s-x%03d-y%03d{image_format}' % (target, x0, y0))

    msgbox.showinfo(title='Info', message='Sixteen images saved successfully !')


def grid_slicer8():
    global opened_image, image_path, image_height, image_width, image_name, image_format
    h_cut = int(round(image_height / 8))
    w_cut = int(round(image_width / 8))

    img = Image.open(image_path)

    new_path = tk_file.askdirectory()
    new_dir = pathlib.Path(new_path, os.path.splitext(image_name)[0] + '/8x8')
    target = new_path + '/' + os.path.splitext(image_name)[0] + '/8x8/' + os.path.splitext(image_name)[0] + '_8x8'
    new_dir.mkdir(parents=True, exist_ok=True)

    for x0 in range(0, image_width, w_cut):
        for y0 in range(0, image_height, h_cut):
            cord = (x0, y0,
                    x0 + w_cut if x0 + w_cut < image_width else image_width - 1,
                    y0 + h_cut if y0 + h_cut < image_height else image_height - 1)
            print('%s %s' % (image_path, cord))

            if (image_width - x0) > 2 and (image_height - y0) > 2:
                img.crop(cord).save(f'%s-x%03d-y%03d{image_format}' % (target, x0, y0))

    msgbox.showinfo(title='Info', message='Sixty Four images saved successfully !')


def save_image():
    if image_path:
        file_name = tk_file.asksaveasfilename()
        if file_name:
            edited_image.save(file_name)


def open_image():
    global opened_image, image_path, image_height, image_width, image_name, image_format

    image_path = tk_file.askopenfilename()

    if image_path:
        opened_image = ImageTk.PhotoImage(Image.open(image_path))
        image_lb.config(image=opened_image)

        image_height = opened_image.height()
        image_width = opened_image.width()
        image_name = os.path.basename(image_path)
        image_format = os.path.splitext(image_name)[1]

    screen.geometry(f'{image_width}x{image_height}')


def clear_image():
    global edited_image, opened_image, image_path, image_name, image_format, image_height, image_width


    edited_image = ''
    opened_image = ''
    image_path = ''
    image_name = ''
    image_format = ''
    image_height = 0
    image_width = 0
    screen.geometry('800x600')


def exit_window():
    exit()

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
    os.chdir(target)
    name = os.path.splitext(image_name)[0] + f'_{roi[0]}_{roi[1]}_{roi[2]}_{roi[3]}' + f'_2ptROI_{twopt}{image_format}'
    cv2.imwrite(name, img_cropped)
    msgbox.showinfo(title='Info', message='2pt ROI image saved Successfully !')
    cv2.destroyWindow('step1>Click and Drag to select. step2>Hit Enter/Space to Save')
    twopt += 1

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
        
        x1 = x-50 if (x-50) >= 0 else 0
        y1 = y-50 if (y-50) >= 0 else 0
        x2 = x+50 if (x+50) <= image_width else image_width
        y2 = y+50 if (y+50) <= image_height else image_height

        cord = (x1, y1, x2, y2)
        print('%s %s' % (image_path, cord))
        img.crop(cord).save(f'%s-x%03d-y%03d1ptROI{onept}{image_format}' % (target, image_width, image_height / 2))

        msgbox.showinfo(title='Info', message='One image saved successfully !')
        cv2.destroyWindow('image')
        onept += 1
        

menu_bar = tk.Menu(screen)
menu_bar.add_command(label='Open', command=open_image)
# menu_bar.add_command(label='Save', command=save_image)
menu_bar.add_command(label='V Slicer', command=v_slice)
menu_bar.add_command(label='H Slicer', command=h_slice)
menu_bar.add_command(label='2X2 Slicer', command=grid_slicer2)
menu_bar.add_command(label='4x4 Slicer', command=grid_slicer4)
menu_bar.add_command(label='8x8 Slicer', command=grid_slicer8)
menu_bar.add_command(label='1pt ROI',command=onepoint_roi)
menu_bar.add_command(label='2pt ROI',command=twopoint_roi)
menu_bar.add_command(label='Clear', command=clear_image)
menu_bar.add_command(label='Exit', command=exit_window)

screen.config(menu=menu_bar)

image_lb = tk.Label(screen, bg='black')
image_lb.pack(fill=tk.BOTH)

screen.mainloop()