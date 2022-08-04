# create the initial variables below
age=28
sex=0
bmi=26.2
num_of_children=3
smoker=0

# Add insurance estimate formula below

insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("The insurance cost for a 28 year old non-smoking woman with 3 kids and a BMI of 26.2 is "+str(insurance_cost)+". ")

# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("Women who are four years older have estimated insurance costs that are " +str(change_in_insurance_cost) +" dollars different.")

# BMI Factor
age -= 4
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("Women who are 3.1 BMI points heavier have estimated insurance costs that are " +str(change_in_insurance_cost) +" dollars different.")

# Male vs. Female Factor
bmi -= 3.1
sex=1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

if change_in_insurance_cost <= 1:
 print ("The estimated change in cost for being a male instead of female is "+str(change_in_insurance_cost) + " dollars. Being male is cheaper for insurance")

elif change_in_insurance_cost >=1:
  print ("The estimated change in cost for being a male instead of female is " + str(change_in_insurance_cost) + " dollars. Being female is cheaper for insurance.")
# Extra Practice

