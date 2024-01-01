# class mobil :
#     def __init__(self, merk, warna, CC):
#         self.__merk = merk
#         self.warna = warna
#         self.CC = CC
    
#     # def tampilkan_merk(self):
#     #     print(f'Merk : {self.__merk}')
# Jip = mobil("Jeep", "Hitam", 3000)
# # Jip.tampilkan_merk()

# print(Jip.merk)
# print(Jip.warna)
# print(Jip.CC)


class MyClass:
    def __init__(self):
        self.__private_var = 10
        self._protected_var = 20
    
    def acess_private_var(self):
        return self.__private_var
    
    def acess_protected_var(self):
        return self._protected_var
    
class AnotherClass:
    def __init__(self, obj):
        # self.__private_var = obj.__private_var
        self._protected_var = obj._protected_var

obj = MyClass()

another_obj = AnotherClass(obj)

print(another_obj._protected_var)
print(obj.acess_private_var())
print(obj.acess_protected_var())
