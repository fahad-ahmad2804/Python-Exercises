#declare 3 variables to store the times for swimming, cycling and running
#name these variables based on the activity they represent
#convert each variable to integer
#use a nested if/elif structure
#add each input using the "+" arithmetic operator to calculate a total time
#use a combination of comparison operators, coupled with the "and" logical operator
#to judge which range the total input falls within
#structure the if/elif statements in ascending order
#print the correct award message based on the total time

swim_time = input("Enter the competitor's Swim time in minutes: ")
swim_time = int(swim_time)
cyc_time = input("Enter the competitor's Cycling time in minutes: ")
cyc_time = int(cyc_time)
run_time = input("Enter the competitor's Run time in minutes: ")
run_time = int(run_time)
if (swim_time + cyc_time + run_time >=0 and swim_time + cyc_time + run_time <=100):
  print("Congratulations! You have been awarded Provincial Colours")
elif (swim_time + cyc_time + run_time >=101 and swim_time + cyc_time + run_time <=105):
    print("Congratulations! You have been awarded Provincial Half Colours")
elif (swim_time + cyc_time + run_time >=106 and swim_time + cyc_time + run_time <=110):
  print("Congratulations! You have been awarded Provincial Scroll")
elif (swim_time + cyc_time + run_time >111):
    print("Thanks for taking part, better luck next time!")