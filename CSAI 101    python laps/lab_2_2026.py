# Name : Farouq Arabi .
#ID: 20251182 . 
#----------------------

# Q_1 : 
# x = int ( input( "Enter a number :" ))

# if x % 2 ==0 :
#     print ("The num is EVEN ")
# else :
#     print ("The num is Odd .")



# Q_2 : 

#print('area') : is invalid command , caz  it is  not  belong to else condition . 


# Q_3 : 
# output is : 
#1
#10
#2
#10 
#3
#10 


# Q_4 : 
# Value of i = 5 .
#Value of x = 15 . 



# Q_5 : 

#a) output is : 
#1
#3
#5
#7



#b) error , coz he did not put the stpes in negativ num .

#c) output is : 
#9
#7
#5
#3

#d) no output !! , coz the stpes = 0 >.





# Q_6 :  Ask your TA about this proble ,i solved it but i was confused .

# N = int(input ( " Enter A num : "))
# sum = 0 
# for i in range (1, N+1) : 
#     sum=+ i**2
#     print (sum) 




# Q_7 :

# num = int ( input (" Enter a num  : "))

# summetion  = 0 
# if num < 0 :
#     print ("The number is negative , =", num )

# else : 
#     for i in range (1, num +1 ) :
#         summetion += i

#     print ("The summation = " , summetion)




# Q_8 :

# N_1 = int ( input ( "Enter first num = "))
# N_2 = int ( input ( "Enter sec. num = "))

# summition = 0 
# conter = 0 
# for i in range (N_1,N_2 +1) :

#     summition += i 
#     conter += 1 
# print (summition)
# Avg = summition /conter
# print (Avg)



#Q_9 :


# N = int ( input( "Enter num o
# f your Elments:  "))
# conter = 0 
# toutal_sum = 0 
# for i in range (1 , N+1): 
#     x = int ( input ("Enter your Element : "))
#     if x > 6 : 
#         conter += 1 
#         toutal_sum += x 
# if conter > 0 :  # recommended from Gemini :)
#     Avg = toutal_sum / conter
#     print ("The Averge of yor Elments =", Avg)    



#Q_10 : 

# N =  input ("Enter A list of numbers: ").split()
# sum_even = 0
# sum_odd = 0
# for i in  (N):

#     int_num = int(i)
   
#     if int_num % 2 ==0 :
#         sum_even += int_num
#     else :
#         sum_odd += int_num

# print ( "the sum of odd nums = " ,sum_odd)
# print ( "the sum of enev nums = " ,sum_even)


#Q_12 :

#this is my code : Not  accurate at all !!
# de_time = float ( input ("Enter Departure time, in 24-hour format :"))
# arrival_time = float ( input ("Enter Arrival time , in 24-hour format.:"))

# trip_time = de_time - arrival_time 
# if trip_time < 0 : 
#     trip_time*= -1
#     print("Trip Time  Is :",trip_time)

#this is gemi's code : super qualified

# dep_str = input("Enter Departure time (HH:MM): ")
# arr_str = input("Enter Arrival time (HH:MM): ")

# dep_hr, dep_min = map(int, dep_str.split(':'))
# arr_hr, arr_min = map(int, arr_str.split(':'))

# dep_total_min = dep_hr * 60 + dep_min
# arr_total_min = arr_hr * 60 + arr_min

# if arr_total_min < dep_total_min:
#     arr_total_min += 24 * 60

# trip_total_min = arr_total_min - dep_total_min

# trip_hr = trip_total_min // 60
# trip_min = trip_total_min % 60

# print(f"Trip time will be {trip_hr} hr and {trip_min} min")




#Q_11 : I forgot it , so i won't solve it.



#Guess Game_Q_13 : 

# import random 
# num = random.randint(10,20)

# for i in range (5):

#     x = int (input ("Guess a num from 10 to 20 \" you have five chance\" : "))

#     if x == num :
#         print ("Well Done:)") 
#         break
#     else :
#         print ("Try again ;(")
# else :
#     print ("Game Over! ")