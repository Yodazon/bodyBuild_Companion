import dallie3 as dall
import user_info as info
from PIL import Image

print('Hello! Welcome to the bodybuilding app, first lets generate your companion')


input = input("What kind of Companion would you like?")

print("Processing your companion now!")
companion = dall.img_gen(input,info.PAT, info.USER_ID, info.APP_ID )
print("Complete!")

print('Wow look at that!')
companion = Image.open(companion)
companion.show()