import xml.etree.ElementTree as Xet
import pandas as pd
import os

def xml_to_csv(input_folder, output_csv):
    cols = ["filename", "class", "bbox"]
    rows = []

    sorted_path = sorted(os.listdir(input_folder))

    for filename in sorted_path:
        if not filename.endswith('.xml'):
            continue
        fullname = os.path.join(input_folder, filename)
        tree = Xet.parse(fullname)
        root = tree.getroot()
        name = root.find("filename").text

        bbox = []
        classes = []

        for i in root.iter("object"):
            class_name = i.find("name").text
            classes.append(class_name)

        for bbx in root.iter("bndbox"):
            xmin = int(bbx.find('xmin').text)
            ymin = int(bbx.find('ymin').text)
            xmax = int(bbx.find('xmax').text)
            ymax = int(bbx.find('ymax').text)

            bbox.append([xmin, ymin, xmax, ymax])

        rows.append({"filename": name,
                     "class": classes,
                     "bbox": bbox})

    df = pd.DataFrame(rows, columns=cols)
    df.to_csv(output_csv, index=False)
    print("Conversion from XML to CSV successful.")


