RGB = []
RGB.append('Red')
RGB.append('Blue')
RGB.append('Green')

#rgb.sort()
#print(RGB)

RGB.remove('Blue')

print(RGB)

RGB.insert(0, 'White')
RGB.append('Black')

print(RGB)

RGB.reverse()

print(RGB)

print(RGB.pop())
print(RGB)
print(RGB.pop(1))
print(RGB)

cnt = RGB.count('Red')

print(cnt)

RGB.append('Red')

cnt = RGB.count('Red')
print(cnt)

RGB.sort() #오름차 순(ASCending)
print(RGB)
RGB.sort(reverse=True) #내림차 순(DESCending)  
print(RGB)
RGB.sort(reverse=False) # 생략 가능
print(RGB)

POY = ['purple', 'orange', 'yellow']

RGB.extend(POY)
print(RGB)

RGB.clear()
print(len(RGB))
