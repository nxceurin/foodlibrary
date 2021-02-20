class Recipe():
    def __init__(self, cc= "not specified", mainType= "not specified", ili=[], dispn= "unnamed", rating="unrated", link=""):
        self.cuisine= cc
        self.ingList= ili
        self.Type= mainType
        self.name= dispn
        self.star= rating
        self.link= link

    def ingl(self):
        print("Ingredients required to prepare", self.name)
        for i in self.ingList:
            print(i)

    def info(self):
        print("Dish name:", self.name)
        print("Rating:", str(self.star)+"/5")
        self.ingl()
        print("\nDish type:", self.Type)
        print("Speciality of:", self.cuisine)
        print("Recipe link:", self.link)

    def match(self, user):
        match= 0
        for x in user:
            if x in self.ingList:
                match+=1
        return match

    def seestat(self, par):
        if par=="ilen": return len(self.ingList)
        elif par=="name": return self.name
        elif par=="ili": return self.ingList
        elif par=="cc": return self.cuisine
        #elif par=="star": return self.star

def showInfo(val):
    if val not in totalret([], 0, True):
        print("Uh-oh! That's not a valid dish name!")
    else:
        for x in mRList:
            if val== x.seestat("name"):
                x.info()
        

def showRecipe():
    for x in mRList:
        print(x.name)

def showIList():
    print("Available ingredients to choose from:", end=" ")
    for x in range(len(mIList)-1):
        print(mIList[x], end=", ")
    print(mIList[-1], "\n")
        
def totalret(userL, par=60, un=False):
    total, reli=0, {}
    for a in mRList:
        matchper= (a.match(userL)/a.seestat("ilen"))*100
        if matchper>=par:
            total+=1
            reli[a.seestat("name")]= matchper
    if un == True: return reli
    else: return total

def addlist(val, par):
    if par==1:
        mRList.append(val)
    elif par==2:
        mIList.append(val)


#demo items : taken from Genshin Impact
almond_tofu= Recipe("Liyue", "Dessert", ["sugar", "milk", "almond"], "Almond Tofu", "3" "https://genshin-impact.fandom.com/wiki/Almond_Tofu")
golden_crab= Recipe("", "Meal", ["egg", "flour", "crab", "salt"], "Golden Crab", "4", "https://genshin-impact.fandom.com/wiki/Golden_Crab")
buoyant_breeze= Recipe("Mondstadt", "Meal", ["carrot", "potato", "onion"], "A Buoyant Breeze", "3" "https://genshin-impact.fandom.com/wiki/A_Buoyant_Breeze")
lotus_egg= Recipe("", "Soup", ["lotus head", "egg", "sugar"], "Lotus Seed and Egg Soup", "3", "https://genshin-impact.fandom.com/wiki/Lotus_Seed_and_Bird_Egg_Soup")
qstir_fry= Recipe("Liyue", "Meal", ["mushroom", "lotus head", "jueyun chili", "cabbage"], "Qingce Stir Fry", "3", "https://genshin-impact.fandom.com/wiki/Qingce_Stir_Fry")
saut_matsu= Recipe("Mondstadt", "Meal", ["matsutake", "flour", "pinecone", "butter"], "Sautéed Matsutake", "3", "https://genshin-impact.fandom.com/wiki/Saut%C3%A9ed_Matsutake")
moon_pie= Recipe("Mondstadt", "Dessert", ["meat", "egg", "butter", "flour"], "Moon Pie", "4", "https://genshin-impact.fandom.com/wiki/Moon_Pie")
jade_parcel= Recipe("Liyue", "Meal", ["lotus head", "jueyun chili", "cabbage", "ham"], "Jade Parcels", "4", "https://genshin-impact.fandom.com/wiki/Jade_Parcels")
tian_meat= Recipe("Liyue", "Meal", ["meat", "sugar", "qingxin", "matsutake"], "Tianshu Meat", "4", "https://genshin-impact.fandom.com/wiki/Tianshu_Meat")
bamboo_shoot=  Recipe("Liyue", "Soup", ["meat", "ham", "bamboo shoot"], "Bamboo Shoot Soup", "3", "https://genshin-impact.fandom.com/wiki/Bamboo_Shoot_Soup")
barb_rtt= Recipe("Mondstadt", "Meal", ["carrot", "potato", "onion"], "Barbatos Ratatouille", "3", "https://genshin-impact.fandom.com/wiki/Barbatos_Ratatouille")
cl_soup= Recipe("Mondstadt", "Soup", ["calla lily", "crab", "mint"], "Calla Lily Seafood Soup", "3", "https://genshin-impact.fandom.com/wiki/Calla_Lily_Seafood_Soup")
ss_sprat= Recipe("Mondstadt", "Meal", ["butter", "fish", "salt", "small lamp grass"], "Sunshine Sprat", "3", "https://genshin-impact.fandom.com/wiki/Sunshine_Sprat")
honey_roast= Recipe("Mondstadt", "Meal", ["meat", "carrot", "sugar"], "Sticky Honey Roast", "3", "https://genshin-impact.fandom.com/wiki/Sticky_Honey_Roast")

global mRList, mIList
mRList= [almond_tofu, golden_crab, buoyant_breeze, lotus_egg, qstir_fry, saut_matsu, moon_pie, jade_parcel, tian_meat, bamboo_shoot, barb_rtt, cl_soup, ss_sprat, honey_roast]
mIList= ["salt", "sugar", "milk", "pepper", "tofu", "almond", "egg", "flour", "crab", "carrot", "potato", "onion", "fish", "mushroom", "cream", "lotus head", "jueyun chili", "cabbage", "matsutake", "pinecone", "butter", "meat", "ham", "qingxin", "bamboo shoot", "calla lily", "mint", "honey"]
mIList= sorted(mIList)