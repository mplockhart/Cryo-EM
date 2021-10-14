def image_list(image_list):
   image_list = open(image_list, "r")
   content_list = image_list.readlines()
   return content_list

total_mrc_files = image_list("full_image_list.txt")
done_tiffs = image_list("Converted_tiff_files.txt")
unconverted_mrc_list = []

for files in total_mrc_files:
    for image in done_tiffs:
        if files[24:-5] == image[:-5]:
            unconverted = ""
            break
        else:
            unconverted = files
    if unconverted != "":
        unconverted_mrc_list.append(unconverted[:-1])

#print(unconverted_mrc_list)
#print(len(unconverted_mrc_list))

output_image_list_file = open("unconverted_mrc_list.txt", "w")
for image in unconverted_mrc_list:
    output_image_list_file.write(image + "\n")
output_image_list_file.close()