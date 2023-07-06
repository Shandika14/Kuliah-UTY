class Cookie:
    def __init__(self, color):
        self.color = color
             
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color
    
        
cookie_one = Cookie('green')
cookie_two = Cookie('blue')
print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_one.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())

#Fungsional
def hitung_tambah(bil1, bil2):
    return bil1 + bil2

# #Prosedural 
def hitung_tambah2(bil1, bil2):
    print(bil1+bil2)
    
#print(hitung_tambah(1,1))
hitung_tambah(1,1)
print(3 - hitung_tambah(1,1))



