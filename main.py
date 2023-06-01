
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt 

def ReadCSV():
  print('Reading Data From CSV File')
  df= pd.read_csv("data.csv")
  print(df.to_string())
  again()

def No_Index():
  print('Reading Data From CSV File Without index values')
  df= pd.read_csv("data.csv",index_col=0)
  print(df.to_string())
  again()
  
def line():
  df= pd.read_csv("data.csv")
  pn=df['Product_Name']
  av=df['Availability']
  sa=df['Stock_Avaliable']
  oh=df['Overhead']
  lp=df['MSRP']
  cp=df['Cost_Price']
  sp=df['Selling_Price']
  qt=df['Qty_Perday']
  plt.xlabel("PRODUCT NAME")
  plt.xticks(rotation='vertical')
  print('select specific line chart as given bellow')
  print('press 1 to print the data for Product Name Vs Availability')
  print('press 2 to print the data for Product Name Vs Stock Avaliable')
  print('press 3 to print the data for Product Name Vs Overhead')
  print('press 4 to print the data for Product Name Vs MSRP')
  print('press 5 to print the data for Product Name Vs Cost Price')
  print('press 6 to print the data for Product Name Vs selling price ')
  print('press 7 to print data for Product Name Vs Quantity Sold')
  print('press 8 to to compare Overhead price,MSRP and Cost Price')
  
  op =int(input('Enter your Choice'))
  
  if op==1:
    plt.ylabel("Availability of Stock in Percentage")
    plt.title("Availability")
    plt.plot(pn,av,color='#4885ed')
    plt.show()
  elif op==2:
    plt.ylabel("Stock avaliable")
    plt.title("Stock avaliable")
    plt.plot(pn,sa,color='#db3236')
    plt.show()
  elif op==3:
    plt.ylabel("Overhead")
    plt.title("Overhead")
    plt.plot(pn,oh,color='#f4c20d')
    plt.show()
  elif op==4:
    plt.ylabel("MSRP")
    plt.title("MSRP")
    plt.plot(pn,lp,color='#3cba54')
    plt.show()
  elif op==5:
    plt.ylabel("Cost Price")
    plt.title("Cost Price")
    plt.plot(pn,cp,color='#535353')
    plt.show()
  elif op==6:
    plt.ylabel("Selling Price")
    plt.title("Selling Price")
    plt.plot(pn,sp,color='#50C7C7')
    plt.show()
  elif op==7:
    plt.ylabel("Quantity Sold")
    plt.title("Quantity Sold per day")
    plt.plot(pn,qt,color='#7E57C2')
    plt.show()

  elif op==8:
    plt.ylabel('Price in INR')
    plt.plot(pn,oh,color='#f4c20d',label='Overhead Price')
    plt.plot(pn,lp,color='#3cba54',label='MSRP')
    plt.plot(pn,cp,color='#535353',label='Cost Price')
    plt.legend()
    plt.show()
  else:
    print('enter valid input')

def bar_plot():
  df= pd.read_csv("data.csv")
  pn=df['Product_Name']
  av=df['Availability']
  sa=df['Stock_Avaliable']
  oh=df['Overhead']
  lp=df['MSRP']
  cp=df['Cost_Price']
  sp=df['Selling_Price']
  qt=df['Qty_Perday']
  plt.xlabel("PRODUCT NAME")
  plt.xticks(rotation='vertical')
  print('select specific bar chart as given bellow')
  print('press 1 to print the data for Product Name Vs Availability')
  print('press 2 to print the data for Product Name Vs Stock Avaliable')
  print('press 3 to print the data for Product Name Vs Overhead')
  print('press 4 to print the data for Product Name Vs MSRP')
  print('press 5 to print the data for Product Name Vs Cost Price')
  print('press 6 to print the data for Product Name Vs selling price ')
  print('press 7 to print data for Product Name Vs Quantity Sold')
  print('press 8 to to compare Overhead price,MSRP and Cost Price')
  
  op =int(input('Enter your Choice'))
  
  if op==1:
    plt.ylabel("Availability of Stock in Percentage")
    plt.title("Availability")
    plt.bar(pn,av,color='#4885ed')
    plt.show()
  elif op==2:
    plt.ylabel("Stock avaliable")
    plt.title("Stock avaliable")
    plt.bar(pn,sa,color='#db3236')
    plt.show()
  elif op==3:
    plt.ylabel("Overhead")
    plt.title("Overhead")
    plt.bar(pn,oh,color='#f4c20d')
    plt.show()
  elif op==4:
    plt.ylabel("MSRP")
    plt.title("MSRP")
    plt.bar(pn,lp,color='#3cba54')
    plt.show()
  elif op==5:
    plt.ylabel("Cost Price")
    plt.title("Cost Price")
    plt.bar(pn,cp,color='#535353')
    plt.show()
  elif op==6:
    plt.ylabel("Selling Price")
    plt.title("Selling Price")
    plt.bar(pn,sp,color='#50C7C7')
    plt.show()
  elif op==7:
    plt.ylabel("Quantity Sold")
    plt.title("Quantity Sold per day")
    plt.bar(pn,qt,color='#7E57C2')
    plt.show()
  elif op==8:
    pn1=np.arange(len(pn))
    width=0.25
    plt.ylabel('Price in INR')
    plt.bar(pn1,oh,width,color='#f4c20d',label='Overhead Price')
    plt.bar(pn1+0.25,lp,width,color='#3cba54',label='MSRP')
    plt.bar(pn1+0.5,cp,width,color='#535353',label='Cost Price')
    plt.bar(pn1+0.75,sp,width,color='#50C7C7',label='Selling Price')
    plt.legend()
    plt.show()
  else:
    print('enter valid input')

def pie_plot():
  df= pd.read_csv("data.csv")
  pn=df['Product_Name']
  av=df['Availability']
  sa=df['Stock_Avaliable']
  oh=df['Overhead']
  lp=df['MSRP']
  cp=df['Cost_Price']
  sp=df['Selling_Price']
  qt=df['Qty_Perday']
  
  print('select specific pie chart as given bellow')
  print('press 1 to print the data for Product Name Vs Availability')
  print('press 2 to print the data for Product Name Vs Stock Avaliable')
  print('press 3 to print the data for Product Name Vs Overhead')
  print('press 4 to print the data for Product Name Vs MSRP')
  print('press 5 to print the data for Product Name Vs Cost Price')
  print('press 6 to print the data for Product Name Vs selling price ')
  print('press 7 to print data for Product Name Vs Quantity Sold')
  
  op =int(input('Enter your Choice'))
  
  if op==1:
    plt.title("Availability")
    plt.pie(av,labels=pn,autopct='%3d%%')
    plt.show()
  elif op==2:
    plt.title("Stock avaliable")
    plt.pie(sa,labels=pn,autopct='%3d%%')
    plt.show()
  elif op==3:
    plt.title("Overhead")
    plt.pie(oh,labels=pn,autopct='%3d%%')
    plt.show()
  elif op==4:
    plt.title("MSRP")
    plt.pie(lp,labels=pn,autopct='%3d%%')
    plt.show()
  elif op==5:
    plt.title("Cost Price")
    plt.pie(cp,labels=pn,autopct='%3d%%')
    plt.show()
  elif op==6:  
    plt.title("Selling Price")
    plt.pie(sp,labels=pn,autopct="%3d%%")
    plt.show()
  elif op==7:
    plt.title('Quantity sold everyday')
    plt.pie(qt,labels=pn,autopct="%3d%%")
    plt.show()
  else:
    print('enter valid input')

def scatter_plot():
  df= pd.read_csv("data.csv")
  pn=df['Product_Name']
  av=df['Availability']
  sa=df['Stock_Avaliable']
  oh=df['Overhead']
  lp=df['MSRP']
  cp=df['Cost_Price']
  sp=df['Selling_Price']
  qt=df['Qty_Perday']
  
  ax=plt.gca()
  ax.scatter(pn,av,color='#4885ed',label='Availability')
  ax.scatter(pn,sa,color='#db3236',label='Stock Avaliable')
  ax.scatter(pn,oh,color='#f4c20d',label='Overhead_Price')
  ax.scatter(pn,lp,color='#3cba54',label='MSRP')
  ax.scatter(pn,cp,color='#535353',label='Cost Price')
  ax.scatter(pn,sp,color='#50C7C7',label='Selling Price')
  ax.scatter(pn,qt,color='#7E57C2',label='Quantity sold perday')
  
  plt.xlabel('PRODUCT NAME')
  plt.xticks(rotation='vertical')
  plt.title('complete scatter chart')
  plt.legend
  plt.show()
  
def top_bottom():
  df= pd.read_csv("data.csv")
  print('select the following option')
  print('press 1 to print top 5 records')
  print('press 2 to print bottom 5 record')
  print('press 3 to print N records from top')
  print('press 4 to print N records from bottom')
  
  op=int(input('enter your choice'))
  
  if op==1:
    print(df.head())
  elif op==2:
    print(df.tail())
  elif op==3:
    n=int(input('how many records you want to print from top'))
    print(df.head(n))
  elif op==4:
    n=int(input('how many records you want to display ftom bottom'))
    print(df.tail(n))
  else :
    print('enter valid input')

def sort_values():
  df= pd.read_csv("data.csv")
  print('select the following option to print')
  print('press 1 arrange the records as per Availability')
  print('press 2 arrange the records as per Stock Avaliable')
  print('press 3 arrange the records as per Overhead')
  print('press 4 arrange the records as per MSRP')
  print('press 5 arrange the records as per Cost Price')
  
  op=int(input("enter your choice"))
  
  if op==1:
    df.sort_values(['Availability'],inplace=True)
    print(df.to_string())
  elif op==2:
    df.sort_values(['Stock_Avaliable'],inplace = True)
    print(df.to_string())
  elif op==3:
    df.sort_values(['Overhead'],inplace= True)
    print(df.to_string())
  elif op==4:
    df.sort_values(['MSRP'],inplace= True)
    print(df.to_string())
  elif op==5:
    df.sort_values(['Cost_Price'],inplace= True)
    print(df.to_string())
  else:
    print('enter valid input')
 
def accounting():
  df= pd.read_csv("data.csv")
  print('Sellect following accounting functions')
  print('press 1 to find the number of product sold every day')
  print('press 2 to find which product sold the most')
  print('press 3 to find which product sold least')
  print('press 4 to calculate the profit of product you want')
  print('press 5 to find next discount according to current sale')
  print('press 6 to find the billing amount for next sale')
  print('press 7 to find Quantity to be order to fulfil the demand')
  print('press 8 to plot the line chart for net profit after overhead')
  
  op=int(input('enter your choice'))
  
  if op==1:
    print(df.loc[ : ,'Product_Name':'Qty_Perday':7])
    
  elif op==2:
    print('The detail of product sold maximum')
    print(df[df['Qty_Perday']==df['Qty_Perday'].max()])
   
  elif op==3:
    print('The detail of product sold least')
    print(df[df['Qty_Perday']==df['Qty_Perday'].min()])
   
  elif op==4:
    p=int(input('enter the product ID to calculate the profit'))
    ovh=df.iloc[p-1:p,4:5]
    cop=df.iloc[p-1:p,6:7]
    slp=df.iloc[p-1:p,7:8]
    prf=(slp.values-(ovh.values + cop.values))
    name=df.iloc[p-1:p,1:2]
    print("profit of ",name.values,"is(INR): ",prf)
   
  elif op==5:
    p=int(input('enter the product ID to calculate the discount for next sale: : '))
    
    #percentage of discount in next sale is
    #((%Availability)/4)*(fraction of product left)
    #This is not general formula.
    #Only used for project purpose
    
    avp=df.iloc[p-1:p,2:3]
    qtytot=df.iloc[p-1:p,3:4]
    qtysol=df.iloc[p-1:p,8:]
    avp4=avp.values/4
    qtyleft=qtytot.values-qtysol.values
    qtyleftfrc=qtyleft/qtytot.values
    newperc=avp4*qtyleftfrc
    
    name=df.iloc[p-1:p,1:2]
    print("Discount in upcoming sale for: ",name.values,'will be (%):',newperc)

  elif op==6:
    p=int(input('enter the product ID to calculate the billing amount for next sale: : '))
    mrp=df.iloc[p-1:p,5:6]
    avp=df.iloc[p-1:p,2:3]
    qtytot=df.iloc[p-1:p,3:4]
    qtysol=df.iloc[p-1:p,8:]
    avp4=avp.values/4
    qtyleft=qtytot.values-qtysol.values
    qtyleftfrc=qtyleft/qtytot.values
    newperc=avp4*qtyleftfrc
    name=df.iloc[p-1:p,1:2]
    newdis=mrp.values*(newperc/100)
    newamt=mrp.values-newdis
    print(name.values,'will be Avaliable for (INR)',newamt)
  elif op==7:
    p=int(input('enter Product Id to find stock to order'))
    stav=df.iloc[p-1:p,3:4]
    stsol=df.iloc[p-1:p,8:]
    stod=stav.values - stsol.values
    name=df.iloc[p-1:p,1:2]
    print(stod," Piece for: ",name.values,"need to order to fill the stock the stock to fulfil demand")
  
  elif op==8:
    ovh=df.iloc[:,4:5]
    cop=df.iloc[:,6:7]
    slp=df.iloc[:,7:8]
    prf=(slp.values-(ovh.values + cop.values))
    df2=df.assign(Profit = prf)
    pn=df['Product_Name']
    pr=df2['Profit']
    plt.xlabel("PRODUCT NAME")
    plt.xticks(rotation='vertical')
    plt.ylabel("Profit")
    plt.title("Profit of Products")
    plt.plot(pn,pr,color='#4885ed')
    plt.show()
  else:
    print('enter valid input')

def data_detail():
  df= pd.read_csv("data.csv")
  print('select from the follwoing option')
  print('press 1 to print the size of the DataFrame')
  print('press 2 to print the Shape of the DataFrame')
  print('press 3 to print the index of the DataFrame ')
  print('press 4 to print the columns of the DataFrame')
  print('press 5 to print the values of the DataFrame')
  print('press 6 to print the diemension of the data')
  print('press 7 to Transpose the DataFrame')
  
  op=int(input("enter your choice"))
   
  if op==1:
    print(df.size)
    
  elif op==2:
    print(df.shape)
    
  elif op==3:
    print(df.index)
    
  elif op==4:
    print(df.columns)
    
  elif op==5:
    print(df.values)
    
  elif op==6:
    print(df.ndim)
    
  elif op==7:
    print(df.T)
  
  else:
    print('enter valid input')
   
def temp_chge():
  df= pd.read_csv("data.csv")
  print('select from the follwoing option to do temporary Change in New DataFrame')
  print('press 1 to add new column as profit')
  print('press 2 to add custom row')
  
  op=int(input('enter your choice: '))
  
  if op==1:
    ovh=df.iloc[:,4:5]
    cop=df.iloc[:,6:7]
    slp=df.iloc[:,7:8]
    prf=(slp.values-(ovh.values + cop.values))
    df2=df.assign(Profit = prf)
    print(df2)
  
  elif op==2:
    print('enter the following detail to add row')
    c1=int(input("P_ID: "))
    c2=(input("Product_Name: "))
    c3=int(input("Availability: "))
    c4=int(input("Stock_Avaliable: "))
    c5=int(input("Overhead: "))
    c6=int(input("MSRP: "))
    c7=int(input("Cost_Price: "))
    c8=int(input("Selling_Price: "))
    c9=int(input("Qty_Perday: "))
    
    df.loc[len(df.index)] =[c1,c2,c3,c4,c5,c6,c8,c9]
    print(df.to_string())

def arthmat():
  df= pd.read_csv("data.csv")
  print('select from the following option ')
  print('press 1 to perform min()')
  print('press 2 to perform max()')
  print('press 3 to perform sum()')
  print('press 4 to perform mean()')
  
  op=int(input('enter your choice: '))
  
  if op==1:
    print('enter column default index from 2-8 to perform action ')
    a=int(input())
    if a==2:
      print(df['Availability'].min())
    elif a==3:
      print(df['Stock_Avaliable'].min())
    elif a==4:
      print(df['Overhead'].min())
    elif a==5:
      print(df['MSRP'].min())
    elif a==6:
      print(df['Cost_Price'].min())
    elif a==7:
      print(df['Selling_Price'].min())
    elif a==8:
      print(df['Qty_Perday'].min())
    else:
      print('enter vaild input')
      
  elif op==2:
    print('enter column default index from 2-8 to perform action ')
    a=int(input())
    if a==2:
      print(df['Availability'].max())
    elif a==3:
      print(df['Stock_Avaliable'].max())
    elif a==4:
      print(df['Overhead'].max())
    elif a==5:
      print(df['MSRP'].max())
    elif a==6:
      print(df['Cost_Price'].max())
    elif a==7:
      print(df['Selling_Price'].max())
    elif a==8:
      print(df['Qty_Perday'].max())
    else:
      print('enter vaild input ')
      
  elif op==3:
    print('enter column default index from 2-8 to perform action ')
    a=int(input())
    if a==2:
      print(df['Availability'].sum())
    elif a==3:
      print(df['Stock_Avaliable'].sum())
    elif a==4:
      print(df['Overhead'].sum())
    elif a==5:
      print(df['MSRP'].sum())
    elif a==6:
      print(df['Cost_Price'].sum())
    elif a==7:
      print(df['Selling_Price'].sum())
    elif a==8:
      print(df['Qty_Perday'].sum())
    else:
      print('enter vaild input ')
      
  elif op==4:
    print('enter column default index from 2-8 to perform action ')
    a=int(input())
    if a==2:
      print(df['Availability'].mean())
    elif a==3:
      print(df['Stock_Avaliable'].mean())
    elif a==4:
      print(df['Overhead'].mean())
    elif a==5:
      print(df['MSRP'].mean())
    elif a==6:
      print(df['Cost_Price'].mean())
    elif a==7:
      print(df['Selling_Price'].mean())
    elif a==8:
      print(df['Qty_Perday'].mean())
    else:
      print('enter vaild input')
      
  else:
    print('enter vaild input')
    
def menue():
  print('ONLINE STORE MANAGEMENT')
  print('Following are the option to manage')
  print("1. Show the List of products")
  print("2. Show the list of products without index")
  print("3. Plot the line Chart")
  print("4. Plot the bar Chart")
  print("5. Plot the pie Chart")
  print("6. plot the scatter Chart")
  print("7. To select the top or bottom values ")
  print("8. To Sort Values accordingly")
  print("9. To Perform various accounting function")
  print("10. To get the detail of the data which is in DataFrame")
  print("11. To add product or profit")
  print("12 To perform Agregate functions")

def again():
  menue() 
  print("Enter serial number to select")
  sel = int(input())

  if sel==1:
    ReadCSV()

  elif sel==2:
    No_Index()

  elif sel==3:
    line()
  
  elif sel==4:
    bar_plot()
  
  elif sel==5:
    pie_plot()
  
  elif sel==6:
    scatter_plot()
  
  elif sel==7:
    top_bottom()
  
  elif sel==8:
    sort_values()

  elif sel==9:
    accounting()
  
  elif sel==10:
    data_detail()
  
  elif sel==11:
    temp_chge()
  
  elif sel==12:
    arthmat()
  
  else:
    print("Enter form above serial Number")
      
again()
      
      
    

    
    
  
    
     
     
     
   
   
    
   
  
    
  

  
  
  
