import math

list1 = ['size', 'occupied', 'prices', 'music', 'location', 'VIP', 'favorite_beer', 'enjoyed']
list2 = ['Large', 'High', 'Expensive', 'Loud', 'Talpiot', 'No', 'No', 'No']
list3 = ['Large', 'High', 'Expensive', 'Loud', 'City-Center', 'Yes', 'No', 'Yes']
list4 = ['Large', 'Moderate', 'Normal', 'Quiet', 'City-Center', 'No', 'Yes', 'Yes']
list5 = ['Medium', 'Moderate', 'Expensive', 'Quiet', 'German-Colony', 'No', 'No', 'No']
list6 = ['Large', 'Moderate', 'Expensive', 'Quiet', 'German-Colony', 'Yes', 'Yes', 'Yes']
list7 = ['Small', 'Moderate', 'Normal', 'Quiet', 'Ein-Karem', 'No', 'No', 'Yes']
list8 = ['Large', 'Low', 'Normal', 'Quiet', 'Ein-Karem', 'No', 'No', 'No']
list9 = ['Small', 'Moderate', 'Cheap', 'Loud', 'Mahane-Yehuda', 'No', 'No', 'Yes']
list10 = ['Medium', 'High', 'Expensive', 'Loud', 'City-Center', 'Yes', 'Yes', 'Yes']
list11 = ['Medium', 'Low', 'Cheap', 'Quiet', 'City-Center', 'No', 'No', 'No']
list12 = ['Large', 'Moderate', 'Cheap', 'Loud', 'Talpiot', 'No', 'Yes', 'No']
list13 = ['Large', 'Low', 'Cheap', 'Quiet', 'Talpiot', 'Yes', 'Yes', 'No']
list14 = ['Medium', 'Moderate', 'Expensive', 'Quiet', 'Mahane-Yehuda', 'No', 'Yes', 'Yes']
list15 = ['Medium', 'High', 'Normal', 'Loud', 'Mahane-Yehuda', 'Yes', 'Yes', 'Yes']
list16 = ['Large', 'Moderate', 'Normal', 'Loud', 'Ein-Karem', 'No', 'Yes', 'Yes']
list17 = ['Small', 'High', 'Normal', 'Quiet', 'German-Colony', 'No', 'No', 'No']
list18 = ['Large', 'High', 'Cheap', 'Loud', 'City-Center', 'No', 'Yes', 'Yes'   ]
list19 = ['Small', 'Low', 'Normal', 'Quiet', 'City-Center', 'No', 'No', 'No']
list20 = ['Medium', 'Low', 'Expensive', 'Loud', 'Mahane-Yehuda', 'No', 'No', 'No']
list21 = ['Medium', 'Moderate', 'Normal', 'Quiet', 'Talpiot', 'No', 'No', 'Yes']
list22 = ['Medium', 'Low', 'Normal', 'Quiet', 'City-Center', 'No', 'No', 'Yes']

heading=['size', 'occupied', 'prices', 'music', 'location', 'VIP', 'favorite_beer','enjoyed']

size = ['Large','Medium','Small']
occupied = ['High','Moderate','Low']
prices = ['Expensive','Normal','Cheap']
music = ['Loud','Quiet']
location = ['Talpiot','City-Center','Mahane-Yehuda','Ein-Karem','German-Colony']
VIP = ['Yes','No']
favorite_beer = ['Yes','No']
enjoyed = ['Yes','No']

training_data=[]
training_data.append(list2)
training_data.append(list3)
training_data.append(list4)
training_data.append(list5)
training_data.append(list6)
training_data.append(list7)
training_data.append(list8)
training_data.append(list9)
training_data.append(list10)
training_data.append(list11)
training_data.append(list12)
training_data.append(list13)
training_data.append(list14)
training_data.append(list15)
training_data.append(list16)
training_data.append(list17)
training_data.append(list18)
training_data.append(list19)
training_data.append(list20)
training_data.append(list21)
training_data.append(list22)

final_dict = { 'size' : ['Large','Medium','Small'],
               'occupied' : ['High','Moderate','Low'],
               'prices' : ['Expensive','Normal' ,'Cheap'],
               'music' : ['Loud','Quiet'],
               'location' : ['Talpiot','City-Center','Mahane-Yehuda','Ein-Karem','German-Colony'],
               'VIP' : ['Yes','No'],
               'favorite_beer' : ['Yes','No'],
               'enjoyed' : ['Yes','No']
             }


decision_column= 'enjoyed'

def info_gain(heading,training_data,calc_attr,decision_column):
    E=0.0
    vFsupport = {'size': {'Large': 0, 'Medium': 0, 'Small': 0},
                 'occupied': {'High': 0, 'Moderate': 0, 'Low': 0},
                 'prices': {'Expensive': 0, 'Normal': 0, 'Cheap': 0},
                 'music': {'Loud': 0, 'Quiet': 0},
                 'location': {'Talpiot': 0, 'City-Center': 0, 'Mahane-Yehuda': 0, 'Ein-Karem': 0, 'German-Colony': 0},
                 'VIP': {'Yes': 0, 'No': 0},
                 'favorite_beer': {'Yes': 0, 'No': 0},
                 'enjoyed': {'Yes': 0, 'No': 0}
                 }
    ind=heading.index(calc_attr)
    for t in training_data:
        vFsupport[calc_attr][t[ind]]+=1.0
    for v in vFsupport[calc_attr].keys():
        P=vFsupport[calc_attr][v]/sum(vFsupport[calc_attr].values())
        dS=[]
        for t in training_data:
            if t[ind]==v:
                dS.append(t)
        E += P*entropy(heading,dS,decision_column)
    #print decision_column
    return (entropy(heading,training_data,decision_column)-E)

def entropy(heading, training_data, decision_column):

    counter=heading.index(decision_column)
    Entropy=0.0
    vFsupport = {'size': {'Large': 0, 'Medium': 0, 'Small': 0},
                 'occupied': {'High': 0, 'Moderate': 0, 'Low': 0},
                 'prices': {'Expensive': 0, 'Normal': 0, 'Cheap': 0},
                 'music': {'Loud': 0, 'Quiet': 0},
                 'location': {'Talpiot': 0, 'City-Center': 0, 'Mahane-Yehuda': 0, 'Ein-Karem': 0, 'German-Colony': 0},
                 'VIP': {'Yes': 0, 'No': 0},
                 'favorite_beer': {'Yes': 0, 'No': 0},
                 'enjoyed': {'Yes': 0, 'No': 0}
                 }

    for t in training_data:
        
        vFsupport[decision_column][t[counter]] +=1.0

    for v in vFsupport[decision_column].values():
        
        if v==0:
            Entropy=0
        else:
            Entropy+= (-v/len(training_data)) * math.log(v/len(training_data),2)

    return Entropy

	def dist(heading,attr):
    index=heading.index(attr)
    #print index,'index'
    #print final_dict[heading[index]]
    return final_dict[heading[index]]

def Parent_Attribute(training_data,heading,decision_column):
  parent = heading[0]
  #heading.remove('enjoyed')
  max_IG = 0
  for h in heading:
      if h!='enjoyed':
          gain = info_gain(heading,training_data,h,decision_column)
          if gain > max_IG:
              max_IG = gain
              parent = h
  return parent


def shorter_tree(training_data,heading,parent,val):
    finalArray = []
    mark = heading.index(parent)
    for i in training_data:
        if(i[mark]==val):
            n = []
            for j in range(0,len(i)):
                if(j!=mark):
                    n.append(i[j])
            finalArray.append(n)
    #print 'f',finalArray
    return finalArray


def dec_tree(training_data,heading,decision_column):
    d=[]
    for t in training_data:
        d.append(t[heading.index(decision_column)])
    if len(set(d))==1:
        return d[0]
    else:
        parent = Parent_Attribute(training_data,heading,decision_column)
        #print 'parent',parent
        d_tree={parent:{}}
        for di in dist(heading,parent):
            short = shorter_tree(training_data,heading,parent,di)
            nList  = heading[:]
            nList.remove(parent)
            #print val
            #print 'Examples', examples
            if len(short)!=0:
                sd_tree=dec_tree(short,nList,decision_column)
            else:
                sd_tree='NIL'
            d_tree[parent][di]=sd_tree
    return d_tree

print dec_tree(training_data,heading,decision_column)


