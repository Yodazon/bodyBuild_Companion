import dallie3 as dall
import user_info as info
import statistics as stat

from PIL import Image

print('Hello! Welcome to the bodybuilding app, first lets generate your companion')


input_image_prompt = input("What kind of Companion would you like?")

print("Processing your companion now!")
image_path = dall.imgGen(input_image_prompt,info.PAT, info.USER_ID, info.APP_ID )
print("Complete!")

print('Wow look at that!')
companion = Image.open(image_path)
companion.show()

stat_check = stat.determineStatView()

stat.statCheck(stat_check)