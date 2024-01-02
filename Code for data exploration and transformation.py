#!/usr/bin/env python
# coding: utf-8

# In[57]:


import pandas as pd

# Read CSV file
data = pd.read_csv('diabetic_data（2）.csv')






# In[44]:


import pandas as pd

# Assuming 'data' is the dataset you've loaded into the DataFrame 'df'
df = pd.DataFrame(data)

# Set the limitations to find the desirable line
d1 = len(df[(df['change'] == 'No') & (df['readmitted'] == 'NO')])
d2 = len(df[(df['change'] == 'No') & (df['readmitted'] == '<30')])
d3 = len(df[(df['change'] == 'No') & (df['readmitted'] == '>30')])
d4 = len(df[(df['change'] == 'Ch') & (df['readmitted'] == 'NO')])
d5 = len(df[(df['change'] == 'Ch') & (df['readmitted'] == '<30')])
d6 = len(df[(df['change'] == 'Ch') & (df['readmitted'] == '>30')])

# Define the total line
total_line = len(df)

# Calculate the percentage of the desirable line over the total line
p1 = (d1 / total_line) * 100
p2 = (d2 / total_line) * 100
p3 = (d3 / total_line) * 100
p4 = (d4 / total_line) * 100
p5 = (d5 / total_line) * 100
p6 = (d6 / total_line) * 100

# Print the actual percentage
print(total_line)
print(f"change 'No' and readmitted 'NO': {p1}%")
print(f"change 'No' and readmitted '<30': {p2}%")
print(f"change 'No' and readmitted '>30': {p3}%")
print(f"change 'Ch' and readmitted 'NO': {p4}%")
print(f"change 'Ch' and readmitted '<30': {p5}%")
print(f"change 'Ch' and readmitted '>30': {p6}%")


# In[23]:


# import the figure plotting code
import matplotlib.pyplot as plt
import numpy as np

#define the two bars
readmission = ["change", "NO change"]
NO = [p1, p4]  # You might want to replace p1, p4 with actual numerical values
less_than_30_days = [p2, p5]  # Fix variable names with underscores
more_than_30_days = [p3, p6]  # Fix variable names with underscores

#define the size of the bar
fig, ax = plt.subplots(figsize=(10, 7))
#define the backfround colour
fig.patch.set_facecolor('white') 
#ax.grid(color='white') 

# Plotting the bars with different colours
ax.bar(readmission, NO, color="darkolivegreen", label="NO")
ax.bar(readmission, less_than_30_days, color="darkgreen", bottom=NO, label="Less than 30 days")
ax.bar(readmission, more_than_30_days, color="darkseagreen", bottom=np.array(less_than_30_days) + np.array(NO), label="More than 30 days")

# Set plot labels and title
ax.set_title("Relationship between readission and Change in diebatic medications", fontsize=15)
ax.set_xlabel("Change condition")
ax.set_ylabel("Percentage")
ax.legend()  # If 'A' is supposed to be the legend label, use ax.legend(["A"])

plt.show()  # Display the plot


# In[45]:


import pandas as pd

# Assuming 'data' is the dataset you've loaded into the DataFrame 'df'
df = pd.DataFrame(data)

# Set the limitations to find the desirable line
d1 = len(df[(df['diabetesMed'] == 'No') & (df['readmitted'] == 'NO')])
d2 = len(df[(df['diabetesMed'] == 'No') & (df['readmitted'] == '<30')])
d3 = len(df[(df['diabetesMed'] == 'No') & (df['readmitted'] == '>30')])
d4 = len(df[(df['diabetesMed'] == 'Yes') & (df['readmitted'] == 'NO')])
d5 = len(df[(df['diabetesMed'] == 'Yes') & (df['readmitted'] == '<30')])
d6 = len(df[(df['diabetesMed'] == 'Yes') & (df['readmitted'] == '>30')])


# Define the total line
total_line = len(df)

# Calculate the percentage of the desirable line over the total line
p1 = (d1 / total_line) * 100
p2 = (d2 / total_line) * 100
p3 = (d3 / total_line) * 100
p4 = (d4 / total_line) * 100
p5 = (d5 / total_line) * 100
p6 = (d6 / total_line) * 100


# Print the actual percentage
print(total_line)
print(f"diabetesMed 'No' and readmitted 'NO': {p1}%")
print(f"diabetesMed 'No' and readmitted '<30': {p2}%")
print(f"diabetesMed 'No' and readmitted '>30': {p3}%")
print(f"diabetesMed 'Yes' and readmitted 'NO': {p4}%")
print(f"diabetesMed 'Yes' and readmitted '<30': {p5}%")
print(f"diabetesMed 'Yes' and readmitted '>30': {p6}%")


# import the figure plotting code
import matplotlib.pyplot as plt
import numpy as np

#define the two bars
readmission = ["Yes", "NO"]
NO = [p4, p1]  # You might want to replace p1, p4 with actual numerical values
less_than_30_days = [p5, p2]  # Fix variable names with underscores
more_than_30_days = [p6, p3]  # Fix variable names with underscores

#define the size of the bar
fig, ax = plt.subplots(figsize=(10, 7))
#define the backfround colour
fig.patch.set_facecolor('white') 
#ax.grid(color='white') 

# Plotting the bars with different colours
ax.bar(readmission, NO, color="darkolivegreen", label="NO")
ax.bar(readmission, less_than_30_days, color="darkgreen", bottom=NO, label="Less than 30 days")
ax.bar(readmission, more_than_30_days, color="darkseagreen", bottom=np.array(less_than_30_days) + np.array(NO), label="More than 30 days")

# Set plot labels and title
ax.set_title("Relationship between readission and Diabetes drug prescription", fontsize=15)
ax.set_xlabel("Diabetes drug prescription")
ax.set_ylabel("Percentage")
ax.legend()  # If 'A' is supposed to be the legend label, use ax.legend(["A"])

plt.show()  # Display the plot


# In[46]:


import pandas as pd

# Assuming 'data' is the dataset you've loaded into the DataFrame 'df'
df = pd.DataFrame(data)

# Set the limitations to find the desirable line
d1 = len(df[(df['metformin-pioglitazone'] == 'No') & (df['readmitted'] == 'NO')])
d2 = len(df[(df['metformin-pioglitazone'] == 'No') & (df['readmitted'] == '<30')])
d3 = len(df[(df['metformin-pioglitazone'] == 'No') & (df['readmitted'] == '>30')])
d4 = len(df[(df['metformin-pioglitazone'] == 'Steady') & (df['readmitted'] == 'NO')])
d5 = len(df[(df['metformin-pioglitazone'] == 'Steady') & (df['readmitted'] == '<30')])
d6 = len(df[(df['metformin-pioglitazone'] == 'Steady') & (df['readmitted'] == '>30')])
d7 = len(df[(df['metformin-pioglitazone'] == 'Up') & (df['readmitted'] == 'NO')])
d8 = len(df[(df['metformin-pioglitazone'] == 'Up') & (df['readmitted'] == '<30')])
d9 = len(df[(df['metformin-pioglitazone'] == 'Up') & (df['readmitted'] == '>30')])
d10 = len(df[(df['metformin-pioglitazone'] == 'Down') & (df['readmitted'] == 'NO')])
d11 = len(df[(df['metformin-pioglitazone'] == 'Down') & (df['readmitted'] == '<30')])
d12 = len(df[(df['metformin-pioglitazone'] == 'Down') & (df['readmitted'] == '>30')])

# Define the total line
total_line = len(df)

# Calculate the percentage of the desirable line over the total line
p1 = (d1 / total_line) * 100
p2 = (d2 / total_line) * 100
p3 = (d3 / total_line) * 100
p4 = (d4 / total_line) * 100
p5 = (d5 / total_line) * 100
p6 = (d6 / total_line) * 100
p7 = (d7 / total_line) * 100
p8 = (d8 / total_line) * 100
p9 = (d9 / total_line) * 100
p10 = (d10 / total_line) * 100
p11 = (d11 / total_line) * 100
p12 = (d12 / total_line) * 100


# In[47]:


# Print the actual percentage
print(total_line)
print(f"metformin-pioglitazone 'No' and readmitted 'NO': {p1}%")
print(f"metformin-pioglitazone 'No' and readmitted '<30': {p2}%")
print(f"metformin-pioglitazone 'No' and readmitted '>30': {p3}%")
print(f"metformin-pioglitazone 'Steady' and readmitted 'NO': {p4}%")
print(f"metformin-pioglitazone'Steady' and readmitted '<30': {p5}%")
print(f"metformin-pioglitazone Steady' and readmitted '>30': {p6}%")
print(f"metformin-pioglitazone 'Up' and readmitted 'NO': {p7}%")
print(f"metformin-pioglitazone 'Up' and readmitted '<30': {p8}%")
print(f"metformin-pioglitazone 'Up' and readmitted '>30': {p9}%")
print(f"metformin-pioglitazone 'Down' and readmitted 'NO': {p10}%")
print(f"metformin-pioglitazone'Down' and readmitted '<30': {p11}%")
print(f"metformin-pioglitazone Down' and readmitted '>30': {p12}%")


# In[48]:


# import the figure plotting code
import matplotlib.pyplot as plt
import numpy as np


# In[51]:


#define the two bars
readmission = ["No","Steady","Up" ,"Down"]
NO = [p1, p4, p7, p10]  # You might want to replace p1, p4 with actual numerical values
less_than_30_days = [p2, p5, p8, p11]  # Fix variable names with underscores
more_than_30_days = [p3, p6, p9, p12]  # Fix variable names with underscores

#define the size of the bar
fig, ax = plt.subplots(figsize=(10, 7))
#define the backfround colour
fig.patch.set_facecolor('white') 
#ax.grid(color='white') 

# Plotting the bars with different colours
ax.bar(readmission, NO, color="darkolivegreen", label="NO")
ax.bar(readmission, less_than_30_days, color="darkgreen", bottom=NO, label="Less than 30 days")
ax.bar(readmission, more_than_30_days, color="darkseagreen", bottom=np.array(less_than_30_days) + np.array(NO), label="More than 30 days")

# Set plot labels and title
ax.set_title("Relationship between readission and change in metformin-pioglitazone", fontsize=15)
ax.set_xlabel("Change in metformin-pioglitazone")
ax.set_ylabel("Percentage")
ax.legend()  # If 'A' is supposed to be the legend label, use ax.legend(["A"])

plt.show()  # Display the plot


# In[89]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read CSV file
data = pd.read_csv('diabetic_data（2）.csv')

# Define all the medicines
medicines = ['metformin','repaglinide','nateglinide','chlorpropamide','glimepiride','acetohexamide','glipizide','glyburide','tolbutamide','pioglitazone','rosiglitazone','acarbose','miglitol','troglitazone','tolazamide','examide','citoglipton','insulin','glyburide-metformin','glipizide-metformin','glimepiride-pioglitazone','metformin-rosiglitazone','metformin-pioglitazone']  # 添加其他药物的名称

# create a vaccume list to fill the percentage
percentages = []

# write a loop to deal all of the medicines
for med in medicines:
    # write the percentage for each medicines
    values_count = data[med].value_counts(normalize=True) * 100
    
    # for none value use o to replace
    for value in ['No', 'Steady', 'Up', 'Down']:
        if value not in values_count:
            values_count[value] = 0
    
    # put the percentage into the value list
    percentages.append([values_count['No'], values_count['Steady'], values_count['Up'], values_count['Down']])

# define medicine name
medication_labels = [med.capitalize() for med in medicines]  # Using the first character

# define the colour 
colors = ["steelblue","dodgerblue", "lightskyblue", "blue"]

# create figure
fig, ax = plt.subplots(figsize=(12, 8))
fig.patch.set_facecolor('white') 

bottom = np.zeros(len(medicines))  # initialise the bottom height

for j in range(len(percentages[0])):
    values = [percentages[i][j] for i in range(len(medicines))]
    ax.bar(medicines, values, color=colors[j], bottom=bottom, label=["No", "Steady", "Up", "Down"][j])
    bottom += np.array(values)  # update the height

# set the title 
ax.set_title("Relationship between readmission and medicines", fontsize=15)
ax.set_xlabel("Name of medicines")
ax.set_ylabel("Percentage")
ax.legend()  

plt.xticks(medicines, medication_labels)  # x axis is the medicine name
plt.xticks(rotation=45)  # rotate name avoid overlap
ax.set_ylim(0, 105) 
plt.tight_layout()  
plt.show()


# In[124]:


import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame containing Race information

# Calculate the counts for different genders
Caucasian_count = len(data[data['race'] == 'Caucasian'])
Asian_count = len(data[data['race'] == 'Asian'])
Afeican_count = len(data[data['race'] == 'Afeican'])
American_count = len(data[data['race'] == 'American'])
Hispanic_count = len(data[data['race'] == 'Hispanic'])
other_count = len(data[data['race'] == 'other_count'])
total_count = len(data)

# Calculate percentages
p1 = (male_count / total_count) * 100
p2 = (female_count / total_count) * 100
p3 = (unknown_count / total_count) * 100

print(f"Percentage Male: {p1}%")
print(f"Percentage Female: {p2}%")
print(f"Percentage Unknown/Invalid: {p3}%")

labels = ['Male', 'Female', 'Unknown/Invalid']
sizes = [p1, p2, p3]  # Portions for the pie chart

# Set the colors
colors = ['gold', 'yellowgreen', 'lightcoral']

# Plot the figure
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Gender distribution')

# Show the plot
plt.axis('equal')  # Ensure it's a circle and not an ellipse
plt.legend(loc='upper right')
plt.show()


# In[115]:


import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame containing Race information

# Calculate the counts for different races
Caucasian_count = len(data[data['race'] == 'Caucasian'])
Asian_count = len(data[data['race'] == 'Asian'])
African_count = len(data[data['race'] == 'African'])
American_count = len(data[data['race'] == 'American'])
Hispanic_count = len(data[data['race'] == 'Hispanic'])
other_count = len(data[data['race'] == 'Other'])

total_count = len(data)

# Calculate percentages
p1 = (Caucasian_count / total_count) * 100
p2 = (Asian_count / total_count) * 100
p3 = (African_count / total_count) * 100
p6 = (American_count / total_count) * 100
p5 = (Hispanic_count / total_count) * 100
p4 = (other_count / total_count) * 100

print(f"Percentage Caucasian: {p1}%")
print(f"Percentage Asian: {p2}%")
print(f"Percentage African: {p3}%")
print(f"Percentage American: {p6}%")
print(f"Percentage Hispanic: {p5}%")
print(f"Percentage Other: {p4}%")

labels = ['Caucasian', 'Asian', 'African', 'other', 'Hispanic', 'America']
sizes = [p1, p2, p3, p4, p5, p6]  # Portions for the pie chart

# Set the colors
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange', 'pink']

# Plot the figure
plt.figure(figsize=(20, 20))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Race distribution')

# Show the plot
plt.axis('equal')  # Ensure it's a circle and not an ellipse
plt.legend() 
plt.show()


# In[125]:


import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame containing max_glu_serum information

# Calculate the counts for different max_glu_serum categories
normal_count = len(data[data['max_glu_serum'] == 'Normal'])
gt_200_count = len(data[data['max_glu_serum'] == '>200'])
gt_300_count = len(data[data['max_glu_serum'] == '>300'])
none_count = len(data[data['max_glu_serum'] == 'None'])

total_count = len(data)

# Calculate percentages
p1 = (normal_count / total_count) * 100
p2 = (gt_200_count / total_count) * 100
p3 = (gt_300_count / total_count) * 100
p4 = (none_count / total_count) * 100

print(f"Percentage Normal: {p1:.2f}%")
print(f"Percentage >200: {p2:.2f}%")
print(f"Percentage >300: {p3:.2f}%")
print(f"Percentage None: {p4:.2f}%")
labels = ['Normal', '>200', 'None', '>300']
sizes = [p1, p2, p4, p3]  # Portions for the pie chart

# Set the colors
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot the figure
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Max Glucose Serum Test')

# Show the plot
plt.axis('equal')  # Ensure it's a circle and not an ellipse
plt.legend(loc='upper right')  # Place legend outside the pie chart
plt.show()


# In[126]:


import matplotlib.pyplot as plt

# Assuming 'data' is your DataFrame containing A1Cresult information

# Calculate the counts for different A1Cresult categories
normal_count = len(data[data['A1Cresult'] == 'Normal'])
gt_8_count = len(data[data['A1Cresult'] == '>8'])
gt_7_count = len(data[data['A1Cresult'] == '>7'])
none_count = len(data[data['A1Cresult'] == 'None'])

total_count = len(data)

# Calculate percentages
p1 = (normal_count / total_count) * 100
p2 = (gt_8_count / total_count) * 100
p3 = (gt_7_count / total_count) * 100
p4 = (none_count / total_count) * 100

print(f"Percentage Normal: {p1:.2f}%")
print(f"Percentage >8: {p2:.2f}%")
print(f"Percentage >7: {p3:.2f}%")
print(f"Percentage None: {p4:.2f}%")

labels = ['Normal', '>8','None', '>7']
sizes = [p1, p2, p4, p3]  # Portions for the pie chart

# Set the colors
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Plot the figure
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('A1Cresult Value')

# Show the plot
plt.axis('equal')  # Ensure it's a circle and not an ellipse
plt.legend(loc='upper right') 
plt.show()


# In[ ]:




