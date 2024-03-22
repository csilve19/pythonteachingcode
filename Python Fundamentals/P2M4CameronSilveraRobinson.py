# [] create The Weather

# [ ] The Weather: import world_mean_team.csv as mean_temp.txt into the Jupyter notebook
import os
os.system("curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt")

# [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
mean_temps = open('mean_temp.txt','a+') 
#Add the weather for Rio
mean_temps.write('\nRio de Janeiro,Brazil,30.0,18.0')

#Grab the column headings
mean_temps.seek(0)
headings = mean_temps.readline()
headings = headings.split(',')

# [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
#Read the remaining lines from the file using a while loop
city_temp = mean_temps.readline().strip('\n')

print("\nCameron Silvera-Robinson")

while city_temp:
    city_temp = city_temp.split(',')
    print('City of',city_temp[0],headings[2],'is', city_temp[2], "Celcius")
    city_temp = mean_temps.readline().strip('\n')

mean_temps.close()