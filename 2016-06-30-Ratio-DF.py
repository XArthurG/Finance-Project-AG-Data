#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os


# In[2]:


mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-0.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0

result = []
for file in os.listdir(mydir):
    if file.endswith("-1.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_1 = sorted(result)
sorted_list_1

result = []
for file in os.listdir(mydir):
    if file.endswith("-2.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_2 = sorted(result)
#sorted_list_2


# In[3]:


length = len(sorted_list_0)

for i in range(length):
    input_date_0 = sorted_list_0[i]
    input_date_1 = sorted_list_1[i]
    input_date_2 = sorted_list_2[i]
    input_date = input_date_0[:-8]
    
    
    
    
    
    
    
    
    
    
    ## BELOW IS THE PROGRAM/CODE TO RETRIEVE ALL RATIOS FOR BS, CSI & CSCF
    
    
    
    
    
    
    print('\n')
    print('\n')
    print(input_date_0)
    
    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)


    col_one_list = file[input_date_0].tolist()
    #col_one_arr = file[input_date_0].to_numpy()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")
    #print(f"\ncol_one_arr:\n{col_one_arr}\ntype:{type(col_one_arr)}")

    #Enter subs

    subs_00 = 'Total liabilities and s'

    subs00 = 'Marketable securities'
    subs01 = 'Cash and cash equivalents'
    subs02 = 'Accounts receivable'
    subs03 = 'Total current a'
    subs04 = 'Total current l'
    subs05 = 'Total assets'
    subs06 = 'Total liabilities'
    subs07 = 'Retained earnings'
    subs08 = 'Total stockholder'
    subs09 = 'Property'
    subs10 = 'Short'
    subs11 = 'Long'
    subs12 = 'Convertible,'
    subs13 = 'and Class B'

    subs14 = 'Prepaid'

    res_00 = [i for i in col_one_list if subs00 in i]
    #print(res_00)
    #file.replace(res_00, "NaN", inplace=True)


    res00 = [i for i in col_one_list if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list if subs05 in i]
    #print(res05)
    res06 = [i for i in col_one_list if subs06 in i]
    #print(res06)
    res07 = [i for i in col_one_list if subs07 in i]
    #print(res07)
    res08 = [i for i in col_one_list if subs08 in i]
    #print(res08)
    res09 = [i for i in col_one_list if subs09 in i]
    #print(res09)
    res10 = [i for i in col_one_list if subs10 in i]
    #print(res10)
    res11 = [i for i in col_one_list if subs11 in i]
    #print(res11)
    res12 = [i for i in col_one_list if subs12 in i]
    #print(res12)
    res13 = [i for i in col_one_list if subs13 in i]
    #print(res13)

    res14 = [i for i in col_one_list if subs14 in i]
    #print(res14)
    
    if len(res00) >= 2:
        res00 = res00[0]
        #print(res00)
    
    if len(res06) >= 2:
        res06 = res06[0]
        #print(res06)
    
    if len(res14) >= 2:
        res14 = res14[0]
        #print(res14)


    file.replace(res00, 
           "Marketable securities", inplace=True)
    file.replace(res01, 
           "Cash and cash equivalents", inplace=True)
    file.replace(res02, 
           "Accounts receivable", inplace=True)
    file.replace(res03, 
           "Current assets", inplace=True)
    file.replace(res04, 
           "Current liabilities", inplace=True)
    file.replace(res05, 
           "Total assets", inplace=True)
    file.replace(res06, 
           "Total liabilities", inplace=True)
    file.replace(res07, 
           "Retained earnings", inplace=True)
    file.replace(res08, 
           "Total stockholder's equity", inplace=True)
    file.replace(res09, 
           "Property, plant and equipment", inplace=True)
    file.replace(res10, 
           "Short-term debt", inplace=True)
    file.replace(res11, 
           "Long-term debt", inplace=True)
    file.replace(res12, 
           "Convertible stocks", inplace=True)
    file.replace(res13, 
           "Class A and Class B stocks", inplace=True)

    file.replace(res14, 
           "Prepaid expenses", inplace=True)
    #file
    #file.loc[file[input_date_0] == 'Marketable securities']
    ## PREPAID EXPENSES DOES NOT EXIST

    file = file[file['Default'].notna()]

    col_one_arr = file.loc[file[input_date_0].isin(['Marketable securities',
                                          'Cash and cash equivalents',
                                          'Accounts receivable',
                                          'Current assets',
                                          'Current liabilities',
                                          'Total assets',
                                          'Total liabilities',
                                          'Retained earnings',
                                          "Total stockholder's equity",
                                          'Property, plant and equipment',
                                          'Short-term debt',
                                          'Long-term debt',
                                          'Convertible stocks',
                                          'Class A and Class B stocks',
                                         'Prepaid expenses'])].to_numpy()

    if res14:
        col_one_arr_01 = col_one_arr
        #print("Prepaid. Expenses exists.")
    else:
        col_one_arr_00 = np.array([['Prepaid expenses', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Prepaid. Expenses has been added.")
        #print(col_one_arr_01)


    if res10:
        col_one_arr_02 = col_one_arr_01
        #print("Short-term Debt exists.")
    else:
        col_one_arr_00 = np.array([['Short-term debt', '0']])
        col_one_arr_02 = np.append(col_one_arr_01,col_one_arr_00, axis=0)
        #print("Short-term Debt has been added.")
        #print(col_one_arr_02)

    if res12:
        col_one_arr_03 = col_one_arr_02
        #print("Convertible Stocks exists.")
    else:
        col_one_arr_00 = np.array([['Convertible stocks', '0']])
        col_one_arr_03 = np.append(col_one_arr_02,col_one_arr_00, axis=0)
        #print("Convertible Stocks has been added.")
        #print(col_one_arr_03)




    col_one_arr_CSI_04 = np.vstack({tuple(row) for row in col_one_arr_03})


    col_one_arr_BS = np.array(sorted(col_one_arr_CSI_04 ,key=lambda x: x[0]))
    #col_one_arr_BS = col_one_arr


    ## CONVERTIBLE STOCKS NEED TO BE DEFINED (MAX) OR *HIGHEST VALUE - IF MULTIPLE

    #obj = len(col_one_arr)
    #np.insert(col_one_arr, obj, ["PE_1", "PE_1_VALUE"], 0)





    #new_arr00 = np.append(col_one_arr, [["PE_1", "PE_1_VALUE"]],0)

    #new_arr01 = np.append(new_arr00, [["PE_1", "PE_1_VALUE"]],0)
    #new_arr02 = np.append(new_arr01, [["PE_2", "PE_2_VALUE"]],0)
    #new_arr03 = np.append(new_arr02, [["PEG_1", "PEG_1_VALUE"]],0)
    #new_arr04 = np.append(new_arr03, [["PEG_2", "PEG_2_VALUE"]],0)
    #new_arr05 = np.append(new_arr04, [["EV", "EB_VALUE"]],0)
    #new_arr06 = np.append(new_arr05, [["EBIT", "EBIT_VALUE"]],0)
    #new_arr07 = np.append(new_arr06, [["EBITDA", "EBITDA_VALUE"]],0)
    #new_arr08 = np.append(new_arr07, [["DE", "DE_VALUE"]],0)
    #new_arr09 = np.append(new_arr08, [["NE", "NE_VALUE"]],0)
    #new_arr10 = np.append(new_arr09, [["QR_1", "QR_1_VALUE"]],0)
    #new_arr11 = np.append(new_arr10, [["QR_2", "QR_2_VALUE"]],0)

    #new_arr12 = np.append(new_arr11, [["DY", "DY_VALUE"]],0)
    #new_arr13 = np.append(new_arr12, [["DPS", "DPS_VALUE"]],0)
    #new_arr14 = np.append(new_arr13, [["EPS", "EPS_VALUE"]],0)
    #new_arr15 = np.append(new_arr14, [["MCAP", "MCAP_VALUE"]],0)
    #new_arr16 = np.append(new_arr15, [["ROE", "ROE_VALUE"]],0)
    #new_arr17 = np.append(new_arr16, [["NetMargin", "NetMargin_VALUE"]],0)
    #new_arr18 = np.append(new_arr17, [["OperatingMargin", "OperatingMargin_VALUE"]],0)

    #new_arr18

    file = pd.read_csv(input_date_1)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
    file = file.dropna()

    col_one_list = file[input_date_1].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    col_one_list[0] = "Additional Info"

    #Enter subs
    Rev = 'Revenues'
    #print(Rev)

    Rev_0 = 'Revenue'
    #print(Rev_0)

    NI = 'Net income'
    #print(NI)
    
    RD = 'Research and development'
    #print(RD)

    subs00 = 'Cost of'
    subs01 = 'Income from operations'
    subs02 = 'Income before'
    subs03 = 'asic'
    subs04 = 'iluted'
    subs05 = 'Less'

    res00 = [i for i in col_one_list if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list if subs05 in i]
    #print(res05)
    
    file.replace(RD, 
           "Research and development", inplace=True)

    file.replace(Rev_0, 
           "Revenues", inplace=True)


    file.replace(Rev, 
           "Revenues", inplace=True)
    file.replace(NI, 
           "Net income", inplace=True)
    file.replace(res00, 
           "Cost of revenues", inplace=True)
    file.replace(res01, 
           "Operating income", inplace=True)
    file.replace(res02, 
           "Income before taxes", inplace=True)
    file.replace(res03, 
           "Basic EPS", inplace=True)
    file.replace(res04, 
           "Diluted EPS", inplace=True)
    file.replace(res05, 
           "Less: Adjustment Payments", inplace=True)


    col_one_arr = file.loc[file[input_date_1].isin(['Revenues',
                                          'Net income',
                                          'Research and development',
                                          'Cost of revenues',
                                          'Research and development',
                                          'Operating income',
                                          'Income before taxes',
                                          'Basic EPS',
                                          'Diluted EPS',
                                         'Less: Adjustment Payments'])].to_numpy()

    #print(col_one_arr)
    #print(res05)
    #print(type(res05))

    if res05:
        col_one_arr_01 = col_one_arr
        #print("Adj. Payments exists.")
    else:
        col_one_arr_00 = np.array([['Less: Adjustment Payments', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Adj. Payments has been added.")
        #print(col_one_arr_01)

    col_one_arr_CSI_00 = np.vstack({tuple(row) for row in col_one_arr_01})
    col_one_arr_CSI_01 = np.array(sorted(col_one_arr_CSI_00 ,key=lambda x: x[0]))
    #print(col_one_arr_CSI_01)

    if ['Net income'] in col_one_arr_CSI_01[6]:
        col_one_arr_CSI_0 = np.delete(col_one_arr_CSI_01, 5, 0)
    else:
        #print('Net income only appears once')
        col_one_arr_CSI_0 = col_one_arr_CSI_01

    #print(col_one_arr_CSI_0)

    col_one_arr_CSI = col_one_arr_CSI_0

    #col_one_arr_BS = np.array(sorted(col_one_arr ,key=lambda x: x[0]))



    #if col_one_arr_CSI.index[col_one_arr_CSI['Net income'] == True].tolist():
    #print('Hello')
    #else:
    #print('Net income Row_Index 6')

    #if col_one_arr_CSI.iloc[6]['Net income']== True:
    #print('Hello')
    #else:
    #print('Net income Row_Index 6')




    #['Net income'] in col_one_arr_CSI[6]

    file = pd.read_csv(input_date_2)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)

    col_one_list_0 = file[input_date_2].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    col_one_list_0[0] = "Additional Info"
    col_one_list = list(dict.fromkeys(col_one_list_0))

    subs00 = 'Net income'
    subs01 = 'Depreciation'
    subs02 = 'Amortization'
    subs03 = 'Prepaid'
    subs04 = 'by operating activities'
    subs05 = 'in investing activities'
    subs06 = 'in financing activities'
    subs07 = 'Purchases of property'

    res00 = [i for i in col_one_list if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list if subs05 in i]
    #print(res05)
    res06 = [i for i in col_one_list if subs06 in i]
    #print(res06)
    res07 = [i for i in col_one_list if subs07 in i]
    #print(res07)

    file.replace(res00, 
           "Net income", inplace=True)
    file.replace(res01, 
           "Depreciation", inplace=True)
    file.replace(res02, 
           "Amortization", inplace=True)
    file.replace(res03, 
           "Prepaid expenses", inplace=True)
    file.replace(res04, 
           "Net cash provided by operating activities", inplace=True)
    file.replace(res05, 
           "Net cash provided by investing activities", inplace=True)
    file.replace(res06, 
           "Net cash provided by financing activities", inplace=True)
    file.replace(res07, 
           "Purchase of property, plant and equipment", inplace=True)

    col_one_arr = file.loc[file[input_date_2].isin(['Net income',
                                          'Depreciation',
                                          'Amortization',
                                          'Prepaid expenses',
                                          'Net cash provided by operating activities',
                                          'Net cash provided by investing activities',
                                          'Net cash provided by financing activities',
                                         'Purchase of property, plant and equipment'])].to_numpy()



    if res03:
        col_one_arr_01 = col_one_arr
        #print("Prepaid. Expenses exists.")
    else:
        col_one_arr_00 = np.array([['Prepaid expenses', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Prepaid. Expenses has been added.")
        #print(col_one_arr_01)


    col_one_arr_CSCF = np.array(sorted(col_one_arr_01 ,key=lambda x: x[0]))

    #print(col_one_arr_BS)

    Accounts_receivable = float(col_one_arr_BS[0,1])
    Cash_and_cash_equivalents = float(col_one_arr_BS[1,1])
    Class_A_and_Class_B_stocks = float(col_one_arr_BS[2,1])
    Convertible_stocks = float(col_one_arr_BS[3,1])
    Current_assets = float(col_one_arr_BS[4,1])
    Current_liabilities = float(col_one_arr_BS[5,1])
    Long_term_debt = float(col_one_arr_BS[6,1])
    Marketable_securities = float(col_one_arr_BS[7,1])
    Prepaid_expenses = float(col_one_arr_BS[8,1])
    Property_plant_and_equipment = float(col_one_arr_BS[9,1])
    Retained_earnings = float(col_one_arr_BS[10,1])
    Short_term_debt = float(col_one_arr_BS[11,1])
    Total_assets = float(col_one_arr_BS[12,1])
    Total_liabilities = float(col_one_arr_BS[13,1])
    Total_stockholder_equity = float(col_one_arr_BS[14,1])

    #print(col_one_arr_CSI)
    
    #Consolidated Statement of Income CSI
    Basic_EPS = float(col_one_arr_CSI[0,1])
    Cost_of_revenues = float(col_one_arr_CSI[1,1])
    Diluted_EPS = float(col_one_arr_CSI[2,1])
    Income_before_taxes = float(col_one_arr_CSI[3,1])
    Adjustment_Payments = float(col_one_arr_CSI[4,1])
    Net_income = float(col_one_arr_CSI[5,1])
    Operating_income = float(col_one_arr_CSI[6,1])
    Research_Development = float(col_one_arr_CSI[7,1])
    Revenues = float(col_one_arr_CSI[8,1])

    #print(col_one_arr_CSCF)
    
    #Consolidated Statement of Cash Flow CSCF
    Net_income_CSCF = float(col_one_arr_CSCF[0,1])
    Depreciation = float(col_one_arr_CSCF[1,1])
    Amortization = float(col_one_arr_CSCF[2,1])
    Prepaid_expenses_CSCF = float(col_one_arr_CSCF[3,1])
    Net_cash_operating_activities = float(col_one_arr_CSCF[4,1])
    Purchase_of_PPE = float(col_one_arr_CSCF[5,1])
    Net_cash_investing_activities = float(col_one_arr_CSCF[6,1])
    Net_cash_financing_activities = float(col_one_arr_CSCF[7,1])


    #Avg Share Price

    file = pd.read_csv('Alphabet Inc.csv')

    ## TRY STATEMENT FOR date_input-29 -28 -27 -26...
    date_prefix = input_date_0[:-8]
    date_ls = ["31", "30", "29", "28"]

    upd_date_0 = date_prefix + date_ls[0]
    upd_date_1 = date_prefix + date_ls[1]
    upd_date_2 = date_prefix + date_ls[2]
    upd_date_3 = date_prefix + date_ls[3]
    
    print(upd_date_0)
    
    print('\n')

    if upd_date_0 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
        #print(upd_date_0 + " exists.")
    else:
        if upd_date_1 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
            #print("Month finishes in -30")
        else:
            if upd_date_2 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
                #print("Month finishes in -29")
            else:
                if upd_date_3 in file.values:
                    col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                    #print("Month finishes in -28")


    Open_P = col_one_arr_P[0,1]
    Close_P = col_one_arr_P[0,-3]

    Avg_P = ((Open_P + Close_P)/2)

    col_one_arr_P_Modified = np.append(col_one_arr_P, [Avg_P])
    col_one_arr_P_Modified

    #Saved Number of Shares Outstanding (res13)

    def listToString(res13): 
        str1 = "" 
        for ele in res13: 
            str1 += ele  
        return str1 

    str00 = listToString(res13)

    str01 = str00.replace(",", "")
    str02 = str(str01.split("; ",1)[1])[0:6]
    Outstanding_shares = int(str02)

    #Retained Earnings -3 months prior .calc(CHANGE)

    #file.loc[file[input_date_0] == 'Retained earnings']
    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[1], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)
    col_one_list = file[input_date_0].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    subs99 = 'Retained earnings'
    res99 = [i for i in col_one_list if subs99 in i]
    col_one_arr = file.loc[file[input_date_0].isin(['Retained earnings'])].to_numpy()
    RE_start = float(col_one_arr[0,1])


    #https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
    #Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close

    #Net Income -3 months prior .calc(CHANGE)

    file = pd.read_csv(input_date_1)
    file = file.drop(file.columns[3:], axis=1)
    file = file.drop(file.columns[1], axis=1)

    file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
    col_one_arr = file.loc[file[input_date_1].isin(['Net income'])].to_numpy()

    NI_start = float(col_one_arr[0,1])

    RE_close = Retained_earnings
    DP_VALUE = (NI_start + RE_start) - RE_close


    #Free Cash Flow FCF - Additional Data from BS & CSCF

    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[1], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)

    file = file[file['Default'].notna()]

    col_one_list = file[input_date_0].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    subs98 = 'Total current a'
    subs97 = 'Total current l'
    subs96 = 'Property'

    res98 = [i for i in col_one_list if subs98 in i]
    res97 = [i for i in col_one_list if subs97 in i]
    res96 = [i for i in col_one_list if subs96 in i]

    str00 = listToString(res98)
    str01 = listToString(res97)
    str02 = listToString(res96)

    file.replace(str00, "Current assets", inplace=True)
    file.replace(str01, "Current liabilities", inplace=True)
    file.replace(str02, "Property, plant and equipment", inplace=True)

    col_one_arr = file.loc[file[input_date_0].isin(["Current assets"])].to_numpy()
    Current_assets_start = float(col_one_arr[0,1])
    col_one_arr = file.loc[file[input_date_0].isin(["Current liabilities"])].to_numpy()
    Current_liabilities_start = float(col_one_arr[0,1])
    col_one_arr = file.loc[file[input_date_0].isin(["Property, plant and equipment"])].to_numpy()
    Property_plant_and_equipment_start = float(col_one_arr[0,1])



    #For OLD Depreciation Value

    file = pd.read_csv(input_date_2)

    file = file.drop(file.columns[3:], axis=1)
    file = file.drop(file.columns[1], axis=1)

    file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)    
    col_one_list = file[input_date_2].tolist()

    col_one_list[0] = "Additional Info"

    subs95 = 'Depreciation'
    res95 = [i for i in col_one_list if subs95 in i]
    str03 = listToString(res95)
    file.replace(str03, "Depreciation", inplace=True)
    col_one_arr = file.loc[file[input_date_2].isin(["Depreciation"])].to_numpy()
    Depreciation_start = float(col_one_arr[0,1])


    #Ratios Equation & Formula


         #Price to Earnings
    #PE_1_VALUE (Calculate EPS using Net Income & Number of shares issues and outstanding)
    #PE_1_VALUE = Avg_P/(Revenues/Class_A_and_Class_B_stocks)
    PE_1_VALUE = Avg_P / (Net_income / Outstanding_shares) / 1000 #Units
    print(PE_1_VALUE)

    #PE_2_VALUE (Calculate PE_2 using Market Price & Diluted EPS [CSI])
    PE_2_0_VALUE = Avg_P / Diluted_EPS
    print(PE_2_0_VALUE)

    PE_2_1_VALUE = Avg_P / Basic_EPS
    print(PE_2_1_VALUE)


    print('\n')

         #Price/Earnings to Growth
    #PEG_1_VALUE (Calculate PEG using Expected Growth Rate as input)     #print('Enter EGR:')
    #MISSING VALUE EGR can only be determined at the present moment using Expected Growth Rate from: Citibank, Goldman Sachs, JPM, MorganStanley, BNP Paribas - Expected EPS Growth
    #Other sources include the Wall Street Journal WSJ and Yahoo Finance


    #PEG_2_VALUE (Calculate from past 3-6-9-12 months growth rate using linear and non-linear regressions)
    #MISSING VALUE Data from the past 3-6-9-12 months
    #Other source: https://www.investopedia.com/terms/p/price-earningsratio.asp


         #EV and EBITDA-related ratios
    EV_1_VALUE = Avg_P * Outstanding_shares
    print(EV_1_VALUE)
    EV_2_VALUE = Avg_P * Class_A_and_Class_B_stocks
    print(EV_2_VALUE)

    EBIT_VALUE = Net_income_CSCF #Interest (N.A)
    print(EBIT_VALUE)
    EBITDA_VALUE = EBIT_VALUE - Depreciation - Amortization
    print(EBITDA_VALUE)

    EV_1_EBITDA_VALUE = EV_1_VALUE / EBITDA_VALUE
    print(EV_1_EBITDA_VALUE)
    EV_2_EBITDA_VALUE = EV_2_VALUE / EBITDA_VALUE
    print(EV_2_EBITDA_VALUE)

    print('\n')

    DE_VALUE = (Long_term_debt + Short_term_debt) / EBITDA_VALUE
    print(DE_VALUE)
    NE_VALUE = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_VALUE
    print(NE_VALUE)
    QR_1_VALUE = (Cash_and_cash_equivalents + Marketable_securities + Accounts_receivable) / Current_liabilities
    print(QR_1_VALUE)
    QR_2_VALUE = (Current_assets - Prepaid_expenses) / Current_liabilities
    print(QR_2_VALUE)

    print('\n')


         #Dividend-related ratios
    EPS_VALUE = (Net_income - Convertible_stocks) / Outstanding_shares
    #https://www.investopedia.com/ask/answers/032515/what-difference-between-earnings-share-and-dividends-share.asp
    print(EPS_VALUE)
    #Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close
    #https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
    DPS_VALUE = DP_VALUE / Outstanding_shares
    print(DPS_VALUE)

    DY_1_VALUE = Net_income / ((RE_close - RE_start) / RE_close) * 4 # for 4 Quarters/Year
    print(DY_1_VALUE) #Approximation. Dividend Yield should be calculated within -12 months, not -3months
    DY_2_VALUE = DPS_VALUE / Avg_P * 1000 #Units
    print(DY_2_VALUE)

    Div_VALUE = -(Net_cash_financing_activities)
    print(Div_VALUE)

    print('\n')


         #Other Ratios (MCAP, ROE, Margins...) Verify Ratio Formulas
    MCAP_VALUE = Avg_P / Outstanding_shares
    print(MCAP_VALUE)
    ROE_VALUE = Net_income / Total_stockholder_equity * 4 # or 4 Quarters/Year :::: Other formula(s) exist
    print(ROE_VALUE)
    NetMargin_VALUE = (Revenues - Cost_of_revenues) / Revenues
    print(NetMargin_VALUE)
    OperatingMargin_VALUE = Net_cash_operating_activities - Revenues
    print(OperatingMargin_VALUE)

    print('\n')


    #MISSING VALUE: Income before Tax for -6 months (Income_before_taxes is only -3 months). Use current Tax Rate
    Tax_VALUE = 1 - (Net_income / Income_before_taxes)
    print(Tax_VALUE)

    FCF_2_VALUE = (Property_plant_and_equipment + (Depreciation/2)) - (Property_plant_and_equipment_start + (Depreciation_start/2)) #CHANGE(CAPEX) also looking at old Depreciation
    print(FCF_2_VALUE)

    #CHANGE(Assets-Liabilities) - ()#CHANGE(CAPEX)
    FCF_0_VALUE = EBIT_VALUE * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_0_VALUE)
    FCF_1_VALUE = Revenues - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_1_VALUE)
    
    RD_VALUE = Research_Development
    print(RD_VALUE)


    ### USE BOTH 'Outstanding_shares' & 'Class_A_and_Class_B_stocks' FOR RELATED RATIOS?
    
    print('\n')
    
    
    d = {input_date_0[:-6]: ['PE_1_VALUE',
                             'PE_2_0_VALUE',
                             'PE_2_1_VALUE',
                             'EV_1_VALUE',
                             'EV_2_VALUE',
                             'EBIT_VALUE',
                             'EBITDA_VALUE',
                             'EV_1_EBITDA_VALUE',
                             'EV_2_EBITDA_VALUE',
                             'DE_VALUE',
                             'QR_1_VALUE',
                             'QR_2_VALUE',
                             'EPS_VALUE',
                             'DPS_VALUE',
                             'DY_1_VALUE',
                             'DY_2_VALUE',
                             'Div_VALUE',
                             'MCAP_VALUE',
                             'ROE_VALUE',
                             'NetMargin_VALUE',
                             'OperatingMargin_VALUE',
                             'Tax_VALUE',
                             'FCF_0_VALUE',
                             'FCF_1_VALUE',
                             'FCF_2_VALUE',
                            'RD_VALUE'], 
         'Financial Ratio /unit': [PE_1_VALUE,
                             PE_2_0_VALUE,
                             PE_2_1_VALUE,
                             EV_1_VALUE,
                             EV_2_VALUE,
                             EBIT_VALUE,
                             EBITDA_VALUE,
                             EV_1_EBITDA_VALUE,
                             EV_2_EBITDA_VALUE,
                             DE_VALUE,
                             QR_1_VALUE,
                             QR_2_VALUE,
                             EPS_VALUE,
                             DPS_VALUE,
                             DY_1_VALUE,
                             DY_2_VALUE,
                             Div_VALUE,
                             MCAP_VALUE,
                             ROE_VALUE,
                             NetMargin_VALUE,
                             OperatingMargin_VALUE,
                             Tax_VALUE,
                             FCF_0_VALUE,
                             FCF_1_VALUE,
                             FCF_2_VALUE,
                            RD_VALUE]}
    
    df= pd.DataFrame(data=d)
    print(df)
    
    filename = input_date_0[:-6] + "-Ratio-DF.csv"
    df.to_csv(filename)


# In[ ]:





# In[ ]:




