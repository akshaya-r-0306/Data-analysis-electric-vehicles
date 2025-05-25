import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("/Users/akshayarajagopal/downloads/Electric_Vehicle_Population_Data.csv")
car_name=[]
cars_sold=[]
cars={}
useable={}
tesla={}
make_model={}
ev_type={}
model_er={}



for i in data["Make"]:
    if i not in cars:
        cars[i]=1
    else:
        cars[i]+=1
for i in cars:
    if cars[i]>1200:
        useable[i]=cars[i]
item=useable.items()
for i in item:
    car_name.append(i[0])
    cars_sold.append(i[1])
for i in range(len(data)):
    if data.loc[i,"Make"]=="TESLA":
       if data.loc[i,"Model"] not in tesla:
          tesla[data.loc[i,"Model"]]=1
       else:
           tesla[data.loc[i,"Model"]]+=1
for i in range(len(data)):
    if data.loc[i,"Make"]=="TESLA":
       if data.loc[i,"Model"] not in model_er:
          model_er[data.loc[i,"Model"]]=data.loc[i,"Electric Range"]
courses = list(model_er.keys())
values = list(model_er.values())
for i in range(len(data)):
    if data.loc[i,"Make"] in car_name:
       if data.loc[i,"Make"] not in make_model:
          make_model[data.loc[i,"Make"]]=data.loc[i,"Electric Range"]
brands = list(cars.keys())
models = list(cars.values())
for i in range(len(data)):
       if data.loc[i,"Electric Vehicle Type"] not in ev_type:
         ev_type[data.loc[i,"Electric Vehicle Type"]]=[data.loc[i,"Make"]]
       else:
           if data.loc[i,"Make"] not in ev_type[data.loc[i,"Electric Vehicle Type"]]:
               ev_type[data.loc[i,"Electric Vehicle Type"]].append(data.loc[i,"Make"])

labels = list(ev_type.keys())
sizes = [len(ev_type[label]) for label in labels]


#pie chart 3
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen'])
plt.title('Distribution of Electric Vehicle Types')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['Model Year'], bins=15, color='orange', edgecolor='black')
plt.xlabel('Model Year')
plt.ylabel('Number of Vehicles')
plt.title('Distribution of Vehicle Model Years')
plt.grid(axis='y')
plt.show()

#bar graph 1
plt.figure(figsize=(10,6))
plt.bar(brands, models, color='blue')
plt.xlabel('Car Brands')
plt.ylabel('Number of Models')
plt.title('Number of Car Models by Brand')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.show()

#pie chart 1
plt.pie(cars_sold,labels=car_name)
plt.figure(figsize=(16,16))
plt.show()
plt.title("Sales share of different brands")

#pie chart 2
plt.pie(tesla.values(),labels=tesla.keys())
plt.title("Tesla car models sales")

  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',width = 0.4)
plt.xlabel("Tesla models")
plt.ylabel("electric range")
plt.title("Tesla model vs electric range")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(data['Model Year'], data['Electric Range'], alpha=0.5, color='red')
plt.xlabel('Model Year')
plt.ylabel('Electric Range (miles)')
plt.title('Electric Range vs. Model Year')
plt.grid(True)
plt.show()


#bar graph 2
sorted_make_model = dict(sorted(make_model.items(), key=lambda item: item[1], reverse=True))
makes = list(sorted_make_model.keys())
ranges = list(sorted_make_model.values())
plt.figure(figsize=(10, 6))
plt.barh(makes, ranges, color='skyblue')
plt.xlabel('Electric Range (miles)')
plt.title('Electric Range of Electric Vehicles by Make/Model (Sorted)')
plt.grid(axis='x')
plt.show()

print("OUTCOMES")
print("1. People are prefering EVs more than the other types of cars")
print("2. Though there are many famous brands like Audi, Hyundai, BMW producing cars, people don't only go by the brand names")
print("3. Tesla is the top selling brand and among its models, model Y and model 3 sold the most")
print("4. Electric range of the cars have increased over the years significantly")
print("5. But Electric range alone is not the deciding factor for buying a car, other features matter")




