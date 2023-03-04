import numpy as np
import math
import itertools
#### support s threshold: the number of baskets containing all items 

class apriori():
    #### define the items and basket
    def __init__(self, filename,s,c):
        self.filename = filename
        self.basketset = []
        self.s = s
        self.c = c
        self.items_locate = {} ### where does each item locate
        self.num_item = 7
        self.left_item = []
        self.store_item = []
   
    #### open the files
    def openfiles(self):
        file = open(self.filename)
        for items in file.readlines():
            temp = items.split()
            self.basketset.append(temp)

    #### calculate how frequent the items appear in the file in C1
    def locateFirstItem(self):
        i = 0
        for basket in self.basketset:
            for items in basket:
                if (items) in self.items_locate:
                    self.items_locate[(items)].add(i)
                else:
                    self.items_locate[(items)] = set()
                    self.items_locate[(items)].add(i)
                    
            i = i + 1

    def L1(self):
        L_1 = []
        for key in self.items_locate.keys():
            if len(self.items_locate[key]) > self.s:
                self.store_item.append(key)
                L_1.append(key)
        return L_1


    def combine2Items(self,L_1):
        new_set = list(itertools.combinations(set(L_1),2))
        #### count the support of combines item and the confidence of all
        for items in new_set:
            support = len(self.items_locate[(items[0])] & self.items_locate[(items[1])])
            if support > self.s:
                conf1 = float(support) / float(len(self.items_locate[(items[0])]))
                conf2 = float(support) / float(len(self.items_locate[(items[1])]))
                if conf1 > self.c and conf2 > self.c:
                    items = tuple(sorted(items))
                    self.items_locate[items] = self.items_locate[(items[0])] & self.items_locate[(items[1])]
                    self.left_item.append(items)
                    self.store_item.append(items)


    def LocatekItems(self,K):
        ele = set(itertools.chain(*self.left_item)) 
        self.left_item = []
        #### C_K
        new_set = list(itertools.combinations(ele,K))
        new_set = self._remove_unused_item(new_set,K)
        #### L_K
        for item in new_set:
            support = self.items_locate[item[0]] & self.items_locate[item[1]]
            for i in range(2,K):
                support = support & self.items_locate[item[i]]
            if len(support) > self.s :
                self.items_locate[item] = support
                self.left_item.append(item)
                self.store_item.append(item)


    def _remove_unused_item(self,new_set,K):
        pruned_set = new_set
        ## for every possible frequent item set
        for item in new_set:
            ele = list(itertools.combinations(item,K-1))
            ### for every sub item set under this frequent item set
            ### check if the sub item set is also frequent item set
            for element in ele:
                ### if we already know this item is not frequent item then we don't need to check
                if item in pruned_set:
                    ### if we know any one of sub item set is not frequent item, then remve this item
                    if element not in self.store_item:
                        pruned_set.remove(item)
                        break
                    ### if not, check
                    else:
                        ### if the confidence of this sub item set is lower-> remove
                        last = tuple(set(item) - set(element))
                        conf = float(len(self.items_locate[tuple(element)])) / float(len(self.items_locate[last[0]]))
                        if(conf < self.c):
                            pruned_set.remove(item)
                            break
     
        return pruned_set
        
    def main(self):
        self.openfiles()
        self.locateFirstItem()
        L_1 = self.L1()
        self.combine2Items(L_1)
        for i in range(2,self.num_item):
            self.LocatekItems(i+1)


        #### print out
        with open("Result.txt","w") as f:
            freq = {1:0}
            for item in self.store_item: 
                printout = str(item) + " appears " + str(len(self.items_locate[item])) +" times.\n"
                f.write(printout)
                
                if isinstance(item,str):
                    freq[1] += 1
                elif isinstance(item,tuple):
                    if len(item) not in freq.keys():
                        freq[len(item)] = 1
                    else:
                        freq[len(item)] += 1

            for num_item in freq.keys():
                print("(" + str(num_item) + "-tuple): number of freq is "+str(freq[num_item]))
   

        
        
                
def main():
    s = int(input("What is the support threshold? "))
    c = float (input("What is the confidence threshold? "))
                           
    FT = apriori('./data/T10I4D100K.dat',s,c)
    FT.main()
    

if __name__ == "__main__":
    main()