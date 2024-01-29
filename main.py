#1
# file = open("data/text.txt", "r")
# i = file.readlines()
# file2 = open("data/text_second.txt", "r")
# j = file2.readlines()
#
# if i == j:
#     print("Files are the same")
# else:
#     print("Files are not the same")
# file.close()
# file2.close()

#2
#Количество всех символов в файле
# file = open("data/file_third.txt", "r")
# s = file.read()
# file_len = len(s)
# file = open("data/result.txt", "w")
# file.write(str(file_len))
# file.close()



# Количество строк
# file = open("data/file_third.txt", "r")
# s = file.readlines()
# count = len(s)
# file = open("data/result.txt", "w")
# file.write(str(count))
# file.close()


#Количество гласных букв
# list = []
# file = open("data/file_third.txt", "r")
# s = file.read()
# for i in s:
#     if i == "a" or "e" or "i" or "a" or "o" or "u":
#         list.append("vowel")
#
# file = open("data/result.txt", "w")
# count = len(list)
# file.write(str(count))
# file.close()

#Количество согласных букв
# list = []
# file = open("data/file_third.txt", "r")
# s = file.read()
# for i in s:
#     if i != "a" or "e" or "i" or "a" or "o" or "u":
#         j = list.append("not vowel")
#
# file = open("data/result.txt", "w")
# count = len(list)
# file.write(str(count))
# file.close()

#Количество цифр(все равно не понимаю что сделать, превращаю i в строку, все равно ошибка)
# file = open("data/file_third.txt", "r")
# s = file.read()
# for i in s:
#     if i.isdigit():
#         i += 1
#
#
# file = open("data/result.txt", "w")
# file.write(str(i))
# file.close()

#3
# file = open("data/text_third.txt", "r")
# i = file.readlines()
# print(i[-1])   #Последняя строка
# i.pop(-1)
# print(i)
# file.close()

#4
# max_len = 0
# file = open("data/text_fourth.txt", "r")
# all_lines = file.readlines()
# for row in all_lines:
#     current_len = len(row)
#     if current_len > max_len:
#         max_len = current_len
# file = open("data/result.txt", "w")
# s = file.write(str(max_len))
# print(s)
# file.close()

#5
# word = input("Input word: ")
# file = open("data/text_fifth.txt", "r")
# i = file.read()
# count = i.count(word)
# print(f"Your word was used {count} times")
# file.close()

#6
# word = input("Input word u want to change: ")
# change_word = input("Input changed word: ")
# file = open("data/text_sixth.txt", "r")
# i = file.read()
# j = i.replace(word, change_word)
# file = open("data/result.txt", "w") #Откроете просто result и там будет result =)
# file.write(j)




