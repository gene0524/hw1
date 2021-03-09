
# Homework 1 Python Data Analysis
_NTHU IPE 107030027_

## Program Setup 

1. Import the module by using `import csv`

2. Read the cwb weather data
   ```
   cwb_filename = '<student_id>.csv'
   data = []
   header = []
   with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
   ```

We can use the code given above to read the data from the csv file.

3. Analyze & store data

   ```
   target_data = list(filter(lambda item: item['HUMD'] != ('-99.000' or '-999.000'), data))
   ```

   By using `filter`, we can eliminate the data with the value of -99 and -999, and store only the desired data on the list.

   `st1 = list(filter(lambda item: item['station_id'] == 'C0A880', target_data))`

   Using similar method, we get 5 lists of the desired 5 stations(st1~st5).

4. Value extracting and calculation
   In order to sum the "HUMD", which is the humidity, we'll have to get the value from the text.
   
   ```
   get_Data = lambda title, Data_list: [sub_Data[title] for sub_Data in Data_list if title in sub_Data]
   ```

   The data in the specific location can be stored using the code above, then by using the function `float`, we are able to receive the value. The function `map`      allows us to get all the data in dictionaries available in a specific list, and the function `sum` simply adds up all the numbers together.

   `sum(map(float,get_Data('HUMD', station)))`
   An variable(h_sum) is assigned for this result.

5. print
   Finally, assign `final_data` with a sequence of station name and the humidity summation, and print the final data by using `print(final_data)`.
   (`round` is also used to limit the digit of the floating point to 3.)

## Results
   After running the program, the results are shown as the following:

**[['C0A880', 20.81], ['C0F9A0', 16.28], ['C0G640', 18.69], ['C0R190', 18.48], ['C0X260', 16.28]]**

