
atm_card=input("insert the atm card")
if atm_card=="right side" or atm_card=="RIGHT SIDE":
     language=input("select language")
     if language=="english" or language=="ENGLISH" or language=="hindi" or language=="HINDI":
        pin=int(input("enter pin"))
        if pin>=1000 and pin<=9999:
            type_option=input("enter transaction option")  
            if type_option=="withdraw" or type_option=="WITHDRAW":
                account_type=input("enter account_type")
                if account_type=="saving" or account_type=="SAVING":
                   press_key=input("enter press_key")
                   if press_key=="ok" or press_key=="OK":
                       amount=int(input("enter amount"))
                       if amount>=500 or amount<=2000 and amount%500==0:
                         a=amount//2000
                         b=amount%2000
                         c=b//500
                         press=input("enter complete press")
                         if press=="cancel" or press=="cross":
                           print("your transaction is succesfull")
                         else:
                             print("cancel button not press")
                       else:
                            print("amount not available")
                   else:
                     print("press not ok")
                else:
                    print("error")
            elif type_option=="balance enquiry" or type_option=="BALANCE ENQUIRY":
                     account_type=input("enter account_type")
                     if account_type=="saving" or account_type=="SAVING":
                         account_no=int(input("enter account no"))
                         if account_no>=123456789765 and account_no<=999999999999:
                            press_key=input("enter press_key")
                            if press_key=="ok" or press_key=="OK":
                               print("balance checking succesfull")
                            else:
                                print("ok button not press")
                         else:
                             print("account number not correct")
                     else:
                         print("error")
            elif type_option=="deposit money" or type_option=="DEPOSIT money":
                    account_type=input("enter account_type")
                    if account_type=="current" or account_type=="saving":
                         account_no=int(input("enter account_no"))
                         if account_no>=100000000000 and account_no<=999999999999:
                            money=int(input("enter money"))
                            if money>=100 and money<=49000:
                              press_key=input("enter press key")
                              if press_key=="ok" or press_key=="OK":
                                 print("you diposit money succesfull")
                              else:
                                  print("press not ok")
                            else:
                                print("money not transfer")
                         else:
                              print("wrong account no")
                    else:
                         print("error")
            elif type_option=="bill pay" or type_option=="Bill pay":
                   account_type=input("enter account_type")
                   if account_type=="saving" or account_type=="current":
                       account_no=int(input("enter account no"))
                       if account_no>=100000000000 and account_no<=999999999999:
                           money=int(input("enter money"))
                           if money>=0 and money<=20000000000:
                              press_key=input("enter press key")
                              if press_key=="ok" or press_key=="ok":
                                 print("bill transation complet")
                              else:
                                   print("press_key not available")
                           else:
                              print("amount not available")
                       else:
                          print("press not ok button")
                   else:
                       print("account_type not available")
            else:
                print("money not available")
        else:
            print("account wrong no")
     else:
         print("type_option error")
             

