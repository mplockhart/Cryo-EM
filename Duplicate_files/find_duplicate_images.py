def image_list(image_list):
   image_list = open(image_list, "r")
   content_list = image_list.readlines()
   return content_list

total_mrc_files = image_list("total_mrc_files.txt")
done_tiffs = image_list("Converted_tiff_files.txt")
unconverted_mrc_list = []
unconverted = ""
for files in total_mrc_files:
    for image in done_tiffs:
        unconverted = ""
        if files[:-5] == image[:-5]:
            unconverted = ""
            break
        else:
            unconverted = files
    unconverted_mrc_list.append(unconverted)