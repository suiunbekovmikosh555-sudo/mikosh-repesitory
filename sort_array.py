def sort_array(source_array):
    # Массивдеги бардык так сандарды тандап, аларды өсүш тартибинде сорттойбуз
    odds = sorted([x for x in source_array if x % 2 != 0])
    
    # Так сандарды сактоо үчүн индекс
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
  
