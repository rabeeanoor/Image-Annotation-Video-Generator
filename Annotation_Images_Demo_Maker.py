import glob
import cv2
import pandas as pd
import os
import natsort
from  xml2csv import  xml_to_csv
# Define a list of classes
classes = ['Safety-Helmet', 'Reflective-Jacket']

def txt_size(text):
    text_size, _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    return text_size

# Sort files using natsort
def file_sorter(filesList):
    fileList = natsort.natsorted(filesList)
    return fileList

# Function to create image annotation demo
def create_annotation_video(img_dir, label_dir, output_video):
    def img_annotation_demo(img_dir, label_dir):
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
                x1, y1, x2, y2 = int(row[4]), int(row[5]), int(row[6]), int(row[7])
                class_name = str(row[3])
                if class_name in classes:
                    # Get class index
                    class_idx = classes.index(class_name)
                    # Get color based on class index
                    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)][class_idx]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    txt_w, txt_h = txt_size(class_name)
                    cv2.rectangle(frame, (x1, y1 + 2), (x1 + txt_w - 50, y1 - txt_h + 12), color, -1)
                    cv2.putText(frame, class_name, (x1, y1), 0, 1, (255, 255, 255), 2, 1)
            frame = cv2.resize((640,640))
            img_array.append(frame)
        return img_array

    out = cv2.VideoWriter(f"{label_dir}/{output_video}", cv2.VideoWriter_fourcc(*'mp4v'), 5.0, (640, 640))
    img_array = img_annotation_demo(img_dir, label_dir)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print('Video file created successfully :)')

def main():
    img_dir = 'dataset/Images'
    label_dir = 'dataset/Labels'
    output_vid = 'D:/mlops/task/vaccum_sealer_demo.mp4'
    output_csv = 'data.csv'

    xml_to_csv(label_dir, output_csv)
    create_annotation_video(img_dir, label_dir, output_vid)

if __name__ == "__main__":
    main()
