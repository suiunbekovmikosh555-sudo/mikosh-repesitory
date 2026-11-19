# mikosh-repesitory
1 задача 
def binary_array_to_number(arr):
    return int("".join(str(bit) for bit in arr), 2)


2 задача 
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


 3 задача
 def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        # Эгер кийинки тамганын коду мурункусунан 1ге чоң болбосо, демек ошол арадагы тамга жетишпейт
        if ord(chars[i + 1]) - ord(chars[i]) > 1:
            return chr(ord(chars[i]) +


4 задача
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle - 1 : middle + 1]
    else:
      
        
 5 задача       
 return s[middle]
def square_digits(num):
    return int("".join(str(int(digit) ** 2) for digit in str(num)))


def sort_array(source_array):
    # Массивдеги бардык так сандарды тандап, аларды өсүш тартибинде сорттойбуз
    odds = sorted([x for x in source_array if x % 2 != 0])
    
6 задача    # Так сандарды сактоо үчүн индекс
    odd_index = 0
    # Жыйынтык үчүн тизме түзөбүз
    result = []
    for x in source_array:
        if x % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(x)
            
return result
  
