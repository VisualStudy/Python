total = 0 # ���� ���� ����

def add_to_total(a, b):
    global total # ���� ���� total ��� ����
    total = a + b # ���� ���� total ����
    
add_to_total(3, 5)
print('�� ���� �� :', total)