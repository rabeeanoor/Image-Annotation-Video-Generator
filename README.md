**Image-Annotation-Video-Generator**

This script, `Annotation Images Demo maker.py`, is designed to create a video demonstration of annotated images. It utilizes OpenCV for image processing, Pandas for handling data, and natsort for sorting file lists naturally. The script consists of several functions and a main execution block:

1. **Classes Definition:** Defines a list of classes such as 'Safety-Helmet' and 'Reflective-Jacket'.

2. **Text Size Function (`txt_size`):** Calculates the size of text based on the font and scale.

3. **File Sorter Function (`file_sorter`):** Sorts files in a directory using natsort to ensure proper file order.

4. **Image Annotation Demo Function (`create_annotation_video`):** Generates a video by annotating images with bounding boxes and class labels. It reads CSV files containing image annotations, retrieves corresponding images, and overlays annotations on them.

5. **Main Function (`main`):** Orchestrates the execution of the script by defining input/output directories, invoking XML to CSV conversion, and initiating the video creation process.

**Testing Script**

The `testing script.py` is another script provided for testing purposes. It also performs image annotation but with some variations in implementation:

1. **File Sorter Function (`file_sorter`):** Similar to the function in the previous script, it sorts CSV files in a directory.

2. **Image Annotation Demo Function (`img_annotation_demo`):** This function reads CSV files containing image annotations, retrieves corresponding images, and overlays annotations on them. However, it directly handles class-specific annotation logic within the function rather than relying on a separate class list.

**XML to CSV Converter (`xml2csv.py`)**

This script provides functionality to convert XML files containing image annotations to CSV format. It parses XML files, extracts relevant information like filenames, class names, and bounding box coordinates, and saves them into a CSV file for easier manipulation and processing.

**Readme**

1. **Purpose:** These scripts facilitate the creation of annotated image demonstrations and the conversion of XML annotation files to CSV format.

2. **Dependencies:** Ensure that the necessary libraries like OpenCV, Pandas, and natsort are installed to execute the scripts successfully.

3. **Execution:** 
   - Place your image dataset in the specified directory structure (Images in `dataset/Images` and annotations in `dataset/Labels`).
   - Execute `Annotation Images Demo maker.py` to generate a video demonstration of annotated images.
   - Execute `testing script.py` for additional testing or customization of annotation logic.
   - Optionally, use `xml2csv.py` to convert XML annotation files to CSV format.

4. **Customization:** Modify the scripts as needed to suit your specific annotation requirements or dataset structure.

5. **Output:** The generated video demonstration will be saved in the specified output directory (`D:/mlops/task/vaccum_sealer_demo.mp4`). Additionally, the CSV file containing image annotations will be generated as specified (`data.csv`).

6. **Note:** Ensure proper file paths and dependencies are configured before execution.
