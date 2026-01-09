# Function 1 Filter Even Numbers from a List
Numbers = (1,2,3,4,5,6,7,8,9,10)
Even_Numbers = sorted([n for n in Numbers if n % 2 == 0])
print(Even_Numbers)

# Function 2 Count_Character_Frequency

def Count_Character_Frequency(Text):
    freq = {}
    for char in Text.lower():
            freq[char] = freq.get(char, 0) + 1
    return freq
Text = "Hello Developer"
Char_freq = Count_Character_Frequency(Text)
print(Char_freq)