import glob
import cv2
import pandas as pd
import os
import natsort

def txt_size(text):
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    return text_size

#1 sorts csv_file
def file_sorter(filesList):
    fileList = natsort.natsorted(filesList)
    return fileList
#2 Image Annotation Demo Maker

def img_anotation_demo(img_dir, label_dir):
    csv_files = glob.glob(label_dir + '/*.csv')
    csv_files = file_sorter(csv_files)
    img_array = []
    for file in csv_files:
        csv_df = pd.read_csv(file)
        f_name = csv_df['filename'][1]
        img_path = os.path.join(img_dir, f_name)
        frame = cv2.imread(img_path)
        for i in range(len(csv_df)):
            row = csv_df.loc[i]
            height, width = row[2], row[1]
            # get bbox dims
            x1, y1, x2, y2 = int(row[4]), int(row[5]), int(row[6]), int(row[7])
            if str(row[3]) == classes == 'Safety-Helmet':
                color = (255, 0, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                txt_w, txt_h = txt_size(str(row[3]))
                cv2.rectangle(frame, (x1, y1+2), (x1 + txt_w-100, y1 - txt_h+12), color, -1)
                cv2.putText(frame, str(row[3]), (x1, y1), 0, 1, (255, 255, 255), 2, 1)

            elif str(row[3]) == 'Reflective-Jacket':
                color = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                txt_w, txt_h = txt_size(str(row[3]))
                cv2.rectangle(frame, (x1, y1+2), (x1 + txt_w-50, y1 - txt_h+12), color, -1)
                cv2.putText(frame, str(row[3]), (x1, y1), 0, 1, (255, 255, 255), 2, 1)

            # elif str(row[3]) == 'close':
            #     color = (0, 0, 255)
            #     cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            #     txt_w, txt_h = txt_size(str(row[3]))
            #     cv2.rectangle(frame, (x1, y1+2), (x1 + txt_w-50, y1 - txt_h+12), color, -1)
            #     cv2.putText(frame, str(row[3]), (x1, y1), 0, 1, (255, 255, 255), 2, 1)

        # append frame to array
        img_array.append(frame)
    return img_array
    # cv2.imshow('image', frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


img_dir = 'dataset/Images'
label_dir = 'dataset/Labels'
fps = 5.0

size = (1920,1080)
# size = (width,height)

output_vid = 'D:/mlops/task/vaccum_sealer_demo.mp4'

# out = cv2.VideoWriter(output_vid, cv2.VideoWriter_fourcc(*'MP4V'),fps, size)
out = cv2.VideoWriter('aaa.mp4',cv2.VideoWriter_fourcc(*'mp4v'),5.0, (1920,1080))
img_array = img_anotation_demo(img_dir,label_dir)
for i in range(len(img_array)):
    out.write(img_array[i])
#
out.release()
print('video file created successfully :)')