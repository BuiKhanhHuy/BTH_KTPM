def cau_1():
    n = int(input('Nhap so nguyen n: '))
    # a
    print(('*' * n + '\n') * n)

    # b
    for i in range(1, n + 1):
        print(i * '*')

    # c
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)

    # d
    for i in range(1, n + 1, 2):
        print(('*' * i).center(n))


class Cau2:
    def min_max(self):
        n = int(input('Nhap vao so nguyen n: '))
        arr = []
        for i in range(0, n):
            arr.append(int(input('Nhap phan tu thu {0}'.format(i + 1))))
        min_number = min(arr)
        max_number = max(arr)
        if min_number < 0:
            print('So am be nhat: ', min_number)
        else:
            print('So am be nhat: ', '*')
        if max_number > 0:
            print('So duong lon nhat: ', max_number)
        else:
            print('So duong lon nhat: ', '*')


class Cau3:
    def __init__(self):
        self.dic = {}

    def them(self, key_en, value_vn):
        if key_en:
            self.dic[key_en] = value_vn
            return True
        return False

    def xuat(self):
        for k, v in self.dic.items():
            print('+ {0} co  nghia la: {1}'.format(k, v))

    def tim_kiem(self, key_en):
        find = self.dic.get(key_en)
        return find

    def xoa(self, key_en):
        if key_en in self.dic:
            del self.dic[key_en]
            return True
        return False

    def menu(self):
        loop = True
        while loop:
            print('\n1. Them vao tu dien')
            print('2. Xuat tu dien')
            print('3. Tim kiem')
            print('4. Xoa tu dien')
            print('Chon phim so 0 thoat')
            try:
                choose = int(input('Chon di ban: '))
            except:
                input('!!!! Da co loi. Du lieu phai la so...\n')
                continue
            else:
                if choose == 1:
                    print('\n======Them tu vao tu dien=======')
                    key_en = input('+ Nhap tu tieng Anh: ')
                    value_vn = input('+ Nhap tu tieng Viet: ')
                    if self.them(key_en=key_en, value_vn=value_vn):
                        input('>> Them thanh cong! Nhan phim bat ki de tiep tuc...\n')
                    else:
                        input('>> Them that bai! Nhan phim bat ki de tiep tuc...\n')
                elif choose == 2:
                    print('\n======Xuat tu dien=======')
                    self.xuat()
                    input('')
                elif choose == 3:
                    key_find = input('Nhap vao tu can tim kiem: ')
                    result = self.tim_kiem(key_find)
                    if result:
                        print('--> {0} co nghia la: {1}'.format(key_find, result))
                        input('>> Da tim kiem thanh cong! Nhan phim bat ky de tiep tuc....\n')
                    else:
                        input('>> Khong tim thay! Nhan phim bat ky de tiep tuc....\n')
                elif choose == 4:
                    key_delete = input('Nhap vao tu tieng Anh can xoa: \n')
                    if self.xoa(key_delete):
                        print('>> Xoa thanh cong! Nhan phim bat ky de tiep tuc...\n')
                    else:
                        print('>> Xoa that bai!!!!!!\n')
                elif choose == 0:
                    loop = False


class Cau4:
    def __init__(self):
        self.employees = [{
                             "ma_nv": '1',
                             "ten_nv": "Nguyen Van A",
                            }, {
                             "ma_nv": '2',
                             "ten_nv": "Duong Trong C",
                            }, {
                             "ma_nv": '3',
                             "ten_nv": "Nguyen Thanh N",
                            }
                        ]

    @staticmethod
    def hien_thi(employees):
        for employee in employees:
            print('+ Ma nhan vien: ', employee.get('ma_nv'))
            print('+ Ten nhan vien:', employee.get('ten_nv'))
            print('\n')

    def hien_thi_danh_sach(self):
        for employee in self.employees:
            print('+ Ma nhan vien: ', employee.get('ma_nv'))
            print('+ Ten nhan vien:', employee.get('ten_nv'))
            print('\n')

    def tim_kiem_theo_ten(self, name):
        find_lists = []
        for employee in self.employees:
            if str(employee.get('ten_nv')).upper().find(name.upper()) >= 0:
                find_lists.append(employee)
        return find_lists

    def xoa_nhan_vien_theo_ma(self, ma_nv):
        for employee in self.employees:
            if employee.get('ma_nv') and str(employee.get('ma_nv')) == str(ma_nv):
                self.employees.remove(employee)
                return True
        return False

    def them_mot_nhan_vien(self,  ma_nv, ten_nv):
        if ma_nv:
            for employee in self.employees:
                if str(employee.get('ma_nv')) == str(ma_nv):
                    return -1, 'Ma nhan vien da ton tai'
            self.employees.append({'ma_nv': ma_nv, 'ten_nv': ten_nv})
            return 1, 'Them thanh cong nhan vien'
        return -1, 'Them khong thanh cong'

    def menu(self):
        loop = True
        while loop:
            print('1. Hien thi danh sach nhan vien')
            print('2. Tim kiem nhan vien theo ten')
            print('3. Xoa nhan vien ')
            print('4. Them nhan vien')
            print('Chon phim so 0 de thoat!')
            choose = int(input('Chon di ban: '))
            if choose == 1:
                print('=========== Danh sach nhan vien ===============')
                self.hien_thi_danh_sach()
                input('>>> Thanh cong. Nhan phim bat ky de tiep tuc...\n')
            elif choose == 2:
                print('=========== Tim kiem ===============')
                name = input('Nhap ten nhan vien can tim kiem: ')
                emps = self.tim_kiem_theo_ten(name)
                if emps is not []:
                    print('--> danh sach nhan vien da tim duoc <--')
                    Cau4.hien_thi(emps)
                    input('--> Thanh cong. Nhan phim bat ky de tiep tuc...')
                else:
                    input('--> Khong tim thay. Nhan phim bat ky de tiep tuc...')
            elif choose == 3:
                print('=========== Xoa nhan vien ===============')
                ma_nv = int(input('Nhap va ma nhan vien can xoa: '))
                if self.xoa_nhan_vien_theo_ma(ma_nv=ma_nv):
                    input('--> Da xoa thanh cong nhan vien co ma {0}. Nhan phim bat ky de tiep tuc...'.format(ma_nv))
                else:
                    input('--> Xoa khong thanh cong. Nhan phim bat ky de tiep tuc...')
            elif choose == 4:
                print('=========== Them nhan vien ===============')
                ma_nv = str(input('Nhap ma nhan vien can them: '))
                ten_nv = str(input('Nhap ten nhan vien can them: '))

                code, message = self.them_mot_nhan_vien(ma_nv=ma_nv, ten_nv=ten_nv)
                input(">>> {0}. Nhan phim bat ky de tiep tuc...".format(message))
            elif choose == 0:
                loop = False


# cau 1
cau_1()

# cau 2
cau2 = Cau2()
cau2.min_max()

# cau 3
cau3 = Cau3()
cau3.menu()

# cau 4
cau4 = Cau4()
cau4.menu()
