def image_list(image_list):
   image_list = open(image_list, "r")
   content_list = image_list.readlines()
   return content_list

print(image_list("Converted_tiff_files.txt"))