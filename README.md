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
  

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

 7 задача
 for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    
return max_sum


8 задача
def find_even_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1
