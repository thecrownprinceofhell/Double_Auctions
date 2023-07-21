from math import sqrt
import numpy as np
import random
T=9;
N=7;
part_s =[];
part_b= [];
class Sellers:
    def __init__(self):
        self.c_valuation = 150+50*random.random();
        self.rp_seller =0;
        self.avg_deal =0;
        self.alpha = 4 + 4*random.random();
        self.reward = 0;
def updateval(t,rp_seller,avg_deal,alpha):
    cval=0;
    if(rp_seller!=0 and t!=0):
        cval= avg_deal - sqrt((alpha*np.log(t))/rp_seller);
    return cval;
class Buyers:
    def __init__(self):
        self.c_valuation=150+50*random.random();
        self.t_valuation = self.c_valuation;
        self.rp_buyer=0;
        self.avg_deal=0;
        self.alpha = 4 + 4*random.random();
        self.reward=0;
def b_updateval(t,rp_buyer,avg_deal,alpha):
    cval =0;
    if(rp_buyer!=0):
        cval= avg_deal + sqrt((alpha*(np.log(t)))/rp_buyer);
    return cval;  
def findprice(sellers, buyers):
    arr=[];
    for seller in sellers:
        arr.append(seller);
    arr1=[];
    for buyer in buyers:
        arr1.append(buyer);
    arr.sort(key= lambda x: x.c_valuation);
    arr1.sort(key = lambda x: x.c_valuation);
    b_index =0;
    s_index=0;
    while b_index<len(arr1) and s_index<len(arr):
        if(arr1[b_index].c_valuation>=arr[s_index].c_valuation):
            part_b.append(arr1[b_index]);
            part_s.append(arr[s_index]);
            b_index = b_index+1;
            s_index =s_index+1;
        else:
            b_index=b_index+1;
    if(len(part_b)!=0 and len(part_s)!=0):
        price=0.5*(part_s[len(part_s)-1].c_valuation + part_b[len(part_b)-1].c_valuation);
    else:
        price=0;
    return price
def run_auction(sellers,buyers):
    global optimum;
    global tot_reward;
    for t in range(T):
        p=findprice(sellers,buyers);
        if(p!=0):
            for i in range(len(part_s)):
                part_s[i].rp_seller = part_s[i].rp_seller +1;
                if(t==0):
                    part_s[i].avg_deal = p;
                else:
                    part_s[i].avg_deal = (part_s[i].avg_deal*(part_s[i].rp_seller-1) + p)/part_s[i].rp_seller;
                part_s[i].c_valuation =updateval(t,part_s[i].rp_seller, part_s[i].avg_deal,part_s[i].alpha);
                part_s[i].reward = part_s[i].reward + p -part_s[i].t_valuation + random.random();
            for i in range(len(part_b)):
                part_b[i].rp_buyer = part_b[i].rp_buyer +1;
                if(t==0):
                    part_b[i].avg_deal =p;
                else:
                    part_b[i].avg_deal = (part_b[i].avg_deal*(part_b[i].rp_buyer-1) + p)/part_b[i].rp_buyer;
                part_b[i].c_valuation = b_updateval(t+1,part_b[i].rp_buyer, part_b[i].avg_deal,part_b[i].alpha)
                part_b[i].reward = part_b[i].reward + part_b[i].t_valuation -p + random.random();
        part_b.clear();
        part_s.clear();
sellers=[Sellers(),Sellers(),Sellers(),Sellers(),Sellers(),Sellers(),Sellers()];
buyers=[Buyers(),Buyers(),Buyers(),Buyers(),Buyers(),Buyers(),Buyers()];
run_auction(sellers,buyers);











    





