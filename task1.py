# Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
# [4,1,78,99,45] >> [1,4,45,78,99]
# num1 = int(input('ƏDƏD DAXİL EDİN 1: '))
# num2 = int(input('ƏDƏD DAXİL EDİN 2: '))
# num3 = int(input('ƏDƏD DAXİL EDİN 3: '))
# num4 = int(input('ƏDƏD DAXİL EDİN 4: '))
# num5 = int(input('ƏDƏD DAXİL EDİN 5: '))

# list = [num1, num2, num3, num4, num5]
# list.sort()
# print(list)

# Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#  Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 
sentence = input('CÜMLƏ ƏLAVƏ EDİN: ')

soz = sentence.split()

for i in range(len(soz)):
    list = list(soz[i])
    list.sort()
    soz[i] = ''.join(list)

result = ' '.join(soz)
print(result)

# Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
# tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
# ilk input== 4   
# ikinci input == 7
# ucuncu input == 2
# dorduncu input == 13
# tebrikler . 4 cehdde 13 reqemeni tapdiz
n = 13
i = 0

while True:
    k = int(input('RƏQƏM DAXİL EDİN: '))
    i += 1

    if (k < n):
        print(' ARTIRIN')
    elif (k > n):
        print('AZALDIN')
    else:
        print(f' SİZ {n} - Nİ {i} CƏHDDƏ TAPDINIZ.')
        break

# 1 ile 100 arasinda sade ededleri print edin. (for loops)
for i in range(1, 100):
    rqm = True
    for j in range(2, i):
        if (i % j == 0):
            rqm = False
            break
    
    if rqm:
        print(i)