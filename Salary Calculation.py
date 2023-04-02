a_salary=float(input('Enter CTC Salary\n'))
EPF=a_salary*0.035
gratuity=a_salary*0.015
gross=a_salary-EPF-gratuity
income_tax=gross*0.025
m_insurance=8000
i_salary=gross-income_tax-m_insurance
print('\nSalary Receipt')
print('Cost to Company        |\t|',a_salary)
print('Gratuity               |\t|',gross)
print('Income tax             |\t|',income_tax)
print('Medical Insurance      |\t|',m_insurance)
print('____________________   |\t| _____________')
print('Inhand Salary          |\t|',i_salary)
print('Monthly Salary         |\t|',round(a_salary/12,2))