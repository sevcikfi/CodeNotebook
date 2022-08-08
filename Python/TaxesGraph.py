import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

INCOME_TAX = 0.15      #15%
INCOME_TAX_MIL = 0.23  #23%
SOCIAL_TAX = 0.065     #6.5%
HEALTH_TAX = 0.045     #4.5%
DPP_PINK = 10000       #10k base
AVERAGE_WAGE = 38911   #MPSV koef
MINIMUM_WAGE = 16200
HEA_OBZP = MINIMUM_WAGE * 0.135
MIL_CUTOFF = AVERAGE_WAGE * 4
OSCV_SOC = np.ceil((AVERAGE_WAGE / 4) * 0.292) #soc insurance 29.2%
OSCV_HEA = np.ceil((AVERAGE_WAGE / 2) * 0.135) #hea insurance 13.5%

OSVC_FIXED = OSCV_HEA + OSCV_SOC * 1.15 + 100

DISCOUNT = 30840 / 12 #changes yearly

def HPP(gross, student=False, income_tax=INCOME_TAX, income_tax_mil=INCOME_TAX_MIL, social_tax=SOCIAL_TAX, health_tax=HEALTH_TAX,\
    mil_cutoff=MIL_CUTOFF, discount=DISCOUNT):
    """
    """
    taxes = []
    if gross < mil_cutoff:
        taxes.append(gross * income_tax)
        taxes.append(gross * social_tax)
    else:
        taxes.append(gross * income_tax_mil)
        taxes.append(mil_cutoff * social_tax)

    #social =
    
    #health = 
    taxes.append(gross * health_tax)
    taxes.append(-discount)
    sum = np.array(taxes).sum()
    if sum < 0:
        return gross
    return gross - sum

def DPP(gross, student=False, income_tax=INCOME_TAX):
    if gross <= DPP_PINK:
        if student:
            return gross
        else:
            return gross * (1 - income_tax)
    return

def OSVC(gross):
    taxes = []
    taxes.append(gross * 0.60 * 0.15)
    taxes.append(OSCV_SOC)
    taxes.append(OSCV_HEA)
    return gross - np.array(taxes).sum()

def OSVC_fixed(gross, osvc_fix=OSVC_FIXED):
    if gross > 83333:
        return OSVC(gross)
    
    diff = gross - osvc_fix
    if diff < 0:
        return 0
    return diff

def make_graph():

    return


if __name__ == "__main__":
    incomes = pd.DataFrame(np.arange(0, 100001, 100), columns=["income"])

    incomes["HPP"] = incomes["income"].apply(HPP)
    incomes["OSVC-fixed"] = incomes["income"].apply(OSVC_fixed)
    incomes["OSVC"] = incomes["income"].apply(OSVC)

    incomes.set_index("income")
    print(incomes.describe())
    #print(incomes.head())
    #print(OSCV_HEA)
    #print(OSCV_SOC)
    
    incomes.plot(x="income", y=["HPP","OSVC-fixed","OSVC"])
    plt.xlabel("Gross income")
    plt.ylabel("Net Income")
    plt.savefig("fig")