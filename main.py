#Rudy
#Garcia

#leave this code or testing won't work
import random, sys
if len(sys.argv)-1:
	random.seed(int(sys.argv(sys.argv[1])))
#########################################################
 
randval= random.randint(1,5)


print("You crack open your cookie and your fortune falls out: \n ")

F_emoticon= ":/"
  
if randval==1:
  print("Help! I’m being held prisoner in a fortune cookie bakery!\n")
  print("please don't eat me either, (they torture our kind every day)")
elif randval==2:
  print('\"You really crack me up.\"\n')
  print("[horrible joke intended]")
elif randval==3:
  print("You are not illiterate.\n")
  print("xD")
elif randval==4:
  print("You will read this and say \"Geez! I could come up with better fortunes than that!\"\n")
  input("What would you like to come up with?\n")
  print(f"\nWell I'm sure your full of bright ideas. Its a bummer I don't have a system for users imputting new fortunes yet {F_emoticon}")
elif randval==5:
  print("This cookie is never gonna give you up, never gonna let you down.\n")
  sec_val= int(input("\n\nDo you wanna get rickrolled?(1 for yes or 2 for no):"))
  if sec_val==1:
    colon_replace= ":"
    print(f"\nHit this link and enjoy the music {colon_replace}")
    print(f"https{colon_replace}//www.youtube.com/watch?v=dQw4w9WgXcQ\n")
  elif sec_val==2:
    print("Tis a bummer m8, but have you a jolly good day!")
eek = random.randint(7,12)
colon_replace= ":"
randnumber1= random.randint(1,99)
randnumber2= random.randint(1,99)
randnumber3= random.randint(1,99)
randnumber4= random.randint(1,99)
randnumber5= random.randint(1,99)
randnumber6= random.randint(1,99)
print(f"\nHere are you lucky numbers{colon_replace}\n{randnumber1} {randnumber2} {randnumber3} {randnumber4} {randnumber5} {randnumber6}")
if eek==7:
  print("\nAdios")
elif eek==8:
  print("\nL8r")
elif eek==9:
  print("\nGoodbye")
elif eek==10:
  print("\nsee you in a while!")
elif eek==11:
  print("\nCome back whenever, I hope you enjoyed this little program")
elif eek==12:
  print("\nAborting sequence...")
