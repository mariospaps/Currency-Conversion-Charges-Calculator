#Convert pounds into euros and see how much you will be charged by the bank
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

def currency_conv():
    url="https://walletinvestor.com/converter/gbp/eur/1"
    client=urlopen(url)
    page_html=client.read()
    client.close()
    page_soup=soup(page_html,"html.parser")
    var=page_soup.findAll("p",{"itemprop":"text"})
    print(var)
    one_gbp_in_euros=float(input("How much in euros is one pound worth? \n"))
    return one_gbp_in_euros


def main():

    gbp=float(input("How many pounds will you need this month?\n"))
    #print(gbp)

    eur_av=float(input("How much money in euros do you have in your bank account?\n"))
    #print(eur_av)

    withdrawl_charge=4 #euros

    eur_needed= currency_conv()*gbp
    eur_needed=float("%0.2f"% (eur_needed))
    print("You are about to withdraw "+str(eur_needed)+" euros")

    conversion_charge= 0.02*eur_needed
    total_charge=withdrawl_charge+conversion_charge
    total_charge=float("%0.2f"% (total_charge))
    print("The total conversion charge is "+str(total_charge)+" euros")

    #minimum conversion charge is 1 euro and maximum is 30 euros
    if(conversion_charge<1):
        conversion_charge=1
    if(conversion_charge>30):
        conversion_charge=30

    if(eur_needed+total_charge>= eur_av):
        diff=(eur_needed+total_charge)-eur_av
        print("You need to withdraw less money, specifically "+ str(diff)+" fewer euros")
    else:
        print("Go ahead and withdraw the "+ str(gbp) +" pounds")
main()
