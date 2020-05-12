import pandas as pd
import matplotlib.pyplot as plt


def bar(f):
    plt.figure(figsize = (10,5))
    plt.bar(f['Date'],f['No of Deaths'])
          #set label
    plt.ylabel('No of Deaths')
    plt.xlabel('Date')
    plt.title('Daily covid 19 deaths in '+ k, fontweight = 'bold')
    plt.show()
print("Time data for no of confirmed death cases of different countries") 
print("For India click 1")   
print("For UK click 2")
print("For USA click 3")
print("For Italy click 4")
print("For Germany click 5")
n=int(input("click the desired country"))
if(n==1):
    df = pd.read_excel (r'C:\Users\Dell\Documents\daily deaths in covid 19.xlsx','india')
    k="India"
elif(n==2):
    df = pd.read_excel (r'C:\Users\Dell\Documents\daily deaths in covid 19.xlsx','uk')    
    k="UK"
elif(n==3):
    df = pd.read_excel (r'C:\Users\Dell\Documents\daily deaths in covid 19.xlsx','usa')
    k="USA"
elif(n==4):
    df = pd.read_excel (r'C:\Users\Dell\Documents\daily deaths in covid 19.xlsx','italy')
    k="Italy"
elif(n==5):
    df = pd.read_excel (r'C:\Users\Dell\Documents\daily deaths in covid 19.xlsx','germany')
    k="Germany"            
print (df)    
bar(df)    