"""
sources: 
    https://www.penize.cz/kalkulacky/vypocet-ciste-mzdy
    https://www.vypocet.cz/cista-mzda
    https://www.cssz.cz/web/cz/osvc-v-pausalnim-rezimu
    https://www.mpsv.cz/socialni-pojisteni
    https://www.finance.cz/544083-pausalni-dan-2023/
    https://www.itnetwork.cz/prace-a-podnikani-v-it/podnikani/jak-zacit-podnikat
    https://spolehlivaucetni.cz/blog/pausalni-vydaje
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

INCOME_TAX = 0.15      #15%
INCOME_TAX_MIL = 0.23  #23%
SOCIAL_TAX = 0.065     #6.5%
HEALTH_TAX = 0.045     #4.5%
EMPLOYER_BASE = 0.25   #25% from the gross in addition
DPP_PINK = 10000       #10k base
#AVERAGE_WAGE = 38911  #for 2022
AVERAGE_WAGE = 40324   #MPSV coefficient
MINIMUM_WAGE = 16200

OSVC_LIMIT_YEAR1 = 1000000 #OSVC limit yearly
OSVC_LIMIT_YEAR2 = 1500000 #OSVC limit yearly
OSVC_LIMIT_YEAR = 2000000 #OSVC limit yearly
OSVC_LIMIT =  int(OSVC_LIMIT_YEAR / 12) #OSVC monthly
HEALTH_OBZP = MINIMUM_WAGE * 0.135
MILLIONAIRE_CUTOFF = AVERAGE_WAGE * 4
OSCV_SOCIAL:float = np.ceil((AVERAGE_WAGE / 4) * 0.292) #soc insurance 29.2%
OSCV_HEALTH:float = np.ceil((AVERAGE_WAGE / 2) * 0.135) #hea insurance 13.5%
OSVC_FIXED = OSCV_HEALTH + OSCV_SOCIAL * 1.15 + 100     #Fix basic
OSVC_FIX2 = 16000   #(25 500 x 0,292 = 7 446 Kč + health + 100)
OSVC_FIX3 = 26000   #(39 000 x 0,292 = 11 388 Kč + health + 100)

DISCOUNT = 30840 / 12 #changes yearly

def HPP(gross, student=False, income_tax=INCOME_TAX, income_tax_mil=INCOME_TAX_MIL, social_tax=SOCIAL_TAX, health_tax=HEALTH_TAX,\
    mil_cutoff=MILLIONAIRE_CUTOFF, discount=DISCOUNT):
    """
    """
    taxes = []
    #social =
    if gross < mil_cutoff:
        taxes.append(gross * income_tax)
        taxes.append(gross * social_tax)
    else:
        taxes.append(gross * income_tax_mil)
        taxes.append(mil_cutoff * social_tax)
    #health
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

def OSVC(gross:float) -> float:
    taxes = []
    taxes.append(gross * 0.60 * 0.15)
    taxes.append(OSCV_SOCIAL)
    taxes.append(OSCV_HEALTH)
    net = gross - np.array(taxes).sum()
    if net < 0: return 0
    return net

def OSVC_fixed_old(gross:float, osvc_fix=5994, osvc_limit=1000000 / 12):
    """pre 2023"""
    if gross > osvc_limit: 
        return gross - (gross * 0.60 * 0.15) - (5994 - 100)
    net = gross - osvc_fix
    if net < 0: return 0
    return net

def OSVC_fixed(gross:float, osvc_fix=OSVC_FIXED, osvc_limit=OSVC_LIMIT, osvc_fix2=OSVC_FIX2, osvc_limit2=OSVC_LIMIT_YEAR2 / 12) -> float:
    if gross > osvc_limit:
        return OSVC(gross)
    if gross > osvc_limit2:
        return gross - osvc_fix2
    net = gross - osvc_fix
    if net < 0:
        return 0
    return net

def make_graph(data : pd.DataFrame):
    #data.plot(x="gross", y=["HPP","OSVC-fixed", "OSVC-fixed-old","OSVC"])
    #plt.grid()
    #plt.xlim(data["gross"].min(), data["gross"].max())
    #plt.xlabel("Gross income")
    #plt.ylabel("Net Income")
    #["0", "minimum wage", "20 000", "country average", "Prague", "60 000", "80 000", "100 000", "120 000", "140 000", "160 000"]
    #ticks = [0, 17300, 20000, 40324, 52213, 60000, 80000, 100000, 120000, 140000, 160000]
    #custom = { 17300: "minimum wage", 40324: "country average", 52213: "Prague"}
    #labels = [custom.get(t, ticks[i]) for i,t in enumerate(ticks)]
    #ax.set_xticklabels(labels)

    fig, axs = plt.subplots(2, 1, figsize=(9,6))
    ax0, ax1 = axs
    ax0.plot(data["gross"], data["HPP"],'-', label="HPP")
    ax0.plot(data["gross"], data["OSVC"], color='tab:green', linestyle='-', label="OSVC VAT")
    ax0.plot(data["gross"], data["OSVC-fixed-old"], color='tab:gray', linestyle=':', label="OSVC fix 2022")
    ax0.plot(data["gross"], data["OSVC-fixed"], color='tab:orange', linestyle='--', label="OSVC fix")
    ax0.set_ylabel("Net Income")
    ax0.set_xlim(data["gross"].min(), data["gross"].max())
    ax0.set_ylim(data["gross"].min())
    ax0.legend()
    #ax0.set_xscale("logit")
    #ax0.set_yscale("log")
    ax0.grid()
    ax0.set_title("Employment vs Freelancing in CZK")

    ax1.plot(data["gross"], data["HPP-tax"], color='tab:blue', linestyle='-', label="HPP")
    ax1.plot(data["gross"], data["HPP-tax-employer"], color='tab:red', linestyle='-', label="HPP+Employer")
    ax1.plot(data["gross"], data["OSVC-tax"], color='tab:green', linestyle='-', label="OSVC VAT")
    ax1.plot(data["gross"], data["OSVC-fixed-old-tax"], color='tab:gray', linestyle=':', label="OSVC fix 2022")
    ax1.plot(data["gross"], data["OSVC-fixed-tax"], color='tab:orange', linestyle='--', label="OSVC fix")
    ax1.set_ylabel("Paid taxes")
    ax1.set_xlim(data["gross"].min(), data["gross"].max())
    ax1.set_ylim(data["gross"].min())
    ax1.legend()
    ax1.set_xlabel("Gross income")
    ax1.grid()
    plt.tight_layout()
    
    return


if __name__ == "__main__":
    incomes = pd.DataFrame(np.arange(0, 175001, 100), columns=["gross"])

    incomes["HPP"] = incomes["gross"].apply(HPP)
    incomes["HPP-tax"] = incomes["gross"] - incomes["HPP"]
    incomes["HPP-tax-employer"] = incomes["HPP-tax"] + incomes["HPP"] * EMPLOYER_BASE

    incomes["OSVC-fixed-old"] = incomes["gross"].apply(OSVC_fixed_old)
    incomes["OSVC-fixed-old-tax"] = incomes["gross"] - incomes["OSVC-fixed-old"]
    incomes["OSVC-fixed"] = incomes["gross"].apply(OSVC_fixed)
    incomes["OSVC-fixed-tax"] = incomes["gross"] - incomes["OSVC-fixed"]

    incomes["OSVC"] = incomes["gross"].apply(OSVC)
    incomes["OSVC-tax"] = incomes["gross"] - incomes["OSVC"]

    incomes.set_index("gross")
    print(incomes.describe())
    make_graph(incomes)
    plt.savefig("fig")
    plt.show()