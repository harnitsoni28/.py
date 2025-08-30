# how many time "the" came in the paragrapgh

from loguru import logger

count = 0   
  
Paragarph = '''The sun was setting over the horizon, casting a golden glow over the landscape. 
The trees swayed gently in the breeze, their leaves rustling softly. 
The birds began to settle in their nests, chirping the last songs of the day.
In the distance, the mountains stood tall and majestic, their peaks kissed by the fading light.
The sky transformed into a canvas of colors, with hues of orange, pink,
and purple blending seamlessly. As the day came to a close, 
the stars started to twinkle one by one, illuminating the night sky. 
It was a moment that reminded everyone of the beauty of nature and the simple joys that life can bring. 
The world felt peaceful, as if time itself had paused to appreciate the splendor of the evening.'''

charList = Paragarph.split(" ") # or LIST() -> change string into list via split or list()

# charList = Paragarph.lower().split(" ")    # We can also convert the words into lower case
# print(charList)

for word in charList:           # check word in list both "the" and "The"
    if(word == "the"):          
        count+=1
    elif(word == "The"):
        count+=1                # inctrement count after finding the and The
    else:
        continue
      
print(count)