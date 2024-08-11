import csv
import pandas as pd

df = pd.read_csv("insurance.csv")

#Regular look up with pandas
average_age = df['age'].mean()
most_common_region = df['region'].mode()[0]

print("The average age of a patient is: " + str(average_age))
print("The most people in the clinic are in the " + str(most_common_region))

#Compare cost between Smoker and Non-Smoker
def average_cost_by_group(group_col, group_one, group_two):
    average_data = df.groupby(group_col)["charges"].mean()
    average_cost_one = average_data.get(group_one, float("nan"))
    average_cost_two = average_data.get(group_two, float("nan"))
    return average_cost_one, average_cost_two

smoker_cost, nonsmoker_cost = average_cost_by_group("smoker", "yes", "no")

print("The average cost for smokers is: $" + str(smoker_cost))
print("The average cost for non-smokers is: $" + str(nonsmoker_cost))

higherCost = 0;
if smoker_cost > nonsmoker_cost:
    higherCost = smoker_cost - nonsmoker_cost
    print("Smokers pay on average $" + str(higherCost) + " more.")
else:
    higherCost = nonsmoker_cost - smoker_cost
    print("Non smokers pay on average $" + str(higherCost) + " more.")

