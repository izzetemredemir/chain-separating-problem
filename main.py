import numpy as np

#number of links of the chain
number_of_chain =7

#Lists represent chains.
traveller_chains = []

#Zeros represent each part of the chain.
liste = np.zeros(number_of_chain).tolist()
traveller_chains.append(liste)
biggset_chain = None
second_biggest_chain = None

#How many times the  chain cutted?
sep_num = 0

def split_chain(chain):

    global second_biggest_chain
    global sep_num
    if(len(chain)==16):
        traveller_chains.remove(chain)
        traveller_chains.append(np.zeros(1).tolist())
        traveller_chains.append(np.zeros(5).tolist())
        traveller_chains.append(np.zeros(10).tolist())
    else:
        if(len(chain)>4):
            traveller_chains.remove(chain)
            traveller_chains.append(np.zeros((len(chain) // 2) - 1).tolist())
            second_biggest_chain = np.zeros((len(chain) // 2) - 1).tolist()
            traveller_chains.append(np.zeros((len(chain) // 2) + 1).tolist())
            traveller_chains.append(np.zeros(1).tolist())
            sep_num += 1
        else:
            traveller_chains.remove(chain)
            for i in range(len(chain)+1):
                sep_num +=1
                traveller_chains.append(np.zeros(1).tolist())
split_chain(liste)
hotel_chanis = []

for a in range(1,number_of_chain+1):

    print("Day :"+str(a)+" Traveller Chains"+str(traveller_chains))
    print("Day :"+str(a)+" Hotel Chains "+str(hotel_chanis))
    chain_status =False
    for i in traveller_chains:
        if len(i)==1:
            chain_status=True
            traveller_chains.remove(i)
            hotel_chanis.append(i)
            break
    if(chain_status!=True):
        for i in traveller_chains:
            temp_list = []
            temp_total = 0
            for x in hotel_chanis:
                temp_list.append(x)
                temp_total += len(x)
                if(len(i)-len(x)==1):
                    traveller_chains.remove(i)
                    hotel_chanis.append(i)
                    hotel_chanis.remove(x)
                    traveller_chains.append(x)
                    chain_status =True
                    break

                elif(len(i)-temp_total==1):
                    traveller_chains.remove(i)
                    hotel_chanis.append(i)
                    for j in temp_list:
                        hotel_chanis.remove(j)
                        traveller_chains.append(j)
                    chain_status = True
                    break

    if(chain_status!=True):
        split_chain(traveller_chains[traveller_chains.index(second_biggest_chain)])
        for i in traveller_chains:
            temp_list = []
            temp_total = 0
            for x in hotel_chanis:
                temp_list.append(x)
                temp_total += len(x)
                if(len(i)-len(x)==1):
                    traveller_chains.remove(i)
                    hotel_chanis.append(i)
                    hotel_chanis.remove(x)
                    traveller_chains.append(x)
                    chain_status =True
                    break

                elif(len(i)-temp_total==1):
                    traveller_chains.remove(i)
                    hotel_chanis.append(i)
                    for j in temp_list:
                        hotel_chanis.remove(j)
                        traveller_chains.append(j)
                    chain_status = True
                    break

print("END")
print("Traveller Chains"+str(traveller_chains))
print("Hotel Chains "+str(hotel_chanis))
print("How many times the  chain cutted :"+str(sep_num) )

