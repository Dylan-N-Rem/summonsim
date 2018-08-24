import random
import time
summon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
ur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
summoned = []
eachsummoned = []
roll = []
ur = 0
sr = 0
r = 0
m = 0
yes = 1
for u1 in range(23):
    roll += ["Crab Long Bao", ]
for u2 in range(61):
    roll += ["Foie Gras", ]
for u3 in range(61):
    roll += ["Peking Duck", ]
for u4 in range(61):
    roll += ["B-52", ]
for u5 in range(62):
    roll += ["Bamboo Rice", ]
for u6 in range(23):
    roll += ["Gingerbread", ]
for u7 in range(5):
    roll += ["Boston Lobster", ]
for u8 in range(5):
    roll += ["Double Scoop", ]
for s1 in range(80):
    roll += ["Tiramisu", ]
for s2 in range(80):
    roll += ["Escargot", ]
for s3 in range(80):
    roll += ["Hotdog", ]
for s4 in range(80):
    roll += ["Mango Pudding", ]
for s5 in range(80):
    roll += ["Hamburger",]
for s6 in range(80):
    roll += ["Steak", ]
for s7 in range(80):
    roll += ["Tangyuan", ]
for s8 in range(80):
    roll += ["Sanma", ]
for s9 in range(80):
    roll += ["Napoleon Cake", ]
for s10 in range(80):
    roll += ["Salad", ]
for s11 in range(80):
    roll += ["Pastel de nata", ]
for s12 in range(80):
    roll += ["Yuxiang", ]
for s13 in range(80):
    roll += ["Sukiyaki", ]
for s14 in range(80):
    roll += ["Brownie", ]
for s15 in range(80):
    roll += ["Red Wine", ]
for s16 in range(80):
    roll += ["Gyoza", ]
for s17 in range(80):
    roll += ["Chocolate", ]
for s18 in range(150):
    roll += ["Eggette", ]
for s19 in range(151):
    roll += ["Pineapple Cake", ]
for r1 in range(413):
    roll += ["Long Bao", ]
for r2 in range(413):
    roll += ["Coffee", ]
for r3 in range(413):
    roll += ["Sashimi", ]
for r4 in range(413):
    roll += ["Macaron", ]
for r5 in range(413):
    roll += ["Zongzi", ]
for r6 in range(413):
    roll += ["Sakuramochi", ]
for r7 in range(413):
    roll += ["Tom Yum", ]
for r8 in range(413):
    roll += ["Taiyaki", ]
for r9 in range(413):
    roll += ["Milk", ]
for r10 in range(413):
    roll += ["Dorayaki", ]
for r11 in range(413):
    roll += ["Sake", ]
for r12 in range(413):
    roll += ["Tempura", ]
for r13 in range(413):
    roll += ["Spicy Gluten", ]
for r14 in range(414):
    roll += ["Jiuniang", ]
for r15 in range(414):
    roll += ["Omurice", ]
for r16 in range(414):
    roll += ["Orange Juice", ]
for r17 in range(414):
    roll += ["Ume Ochazuke" ,]
for r18 in range(414):
    roll += ["Miso Soup" ,]
for r19 in range(414):
    roll += ["Yellow Wine", ]
for m1 in range(46):
    roll += ["Skewer", ]
for m2 in range(46):
    roll += ["Jello", ]
for m3 in range(46):
    roll += ["Pancake", ]
for m4 in range(47):
    roll += ["Popcorn", ]
time.sleep(1)
print("Made by Master Attendant Dylan. UID: 104209")
time.sleep(3)
print("Welcome, fellow Master Attendant!")
time.sleep(3)
print("This is a simulator on summoning food souls!")
time.sleep(3)
print("Please note that this is only a simulator and summons in here will NOT affect your in-game experience.")
time.sleep(3)
while yes != 2:
    ag = 0
    summons = input("Enter the amount of times you want to summon: ")
    if not(summons.isdigit()):
        print("Error - Invalid input: Must be a positive integer")
    elif int(summons) <= 0:
        print("Error - Invalid number: Must be more than 0")
    elif int(summons) >= 1:
        print("Summoning food souls...")
        time.sleep(5)
        summons = int(summons)
        for x in range(summons):
            foodsoul = random.choice(roll)
            summoned += [foodsoul, ]
            if foodsoul in ur_pool:
                ur += 1
            elif foodsoul in sr_pool:
                sr += 1
            elif foodsoul in r_pool:
                r += 1
            elif foodsoul in m_pool:
                m += 1
        eachsummoned = set(summoned) & set(summon_pool)
        eachsummoned = list(eachsummoned)
        ursummoned = set(eachsummoned) & set(ur_pool)
        ursummoned = list(ursummoned)
        ursummoned.sort()
        srsummoned = set(eachsummoned) & set(sr_pool)
        srsummoned = list(srsummoned)
        srsummoned.sort()
        rsummoned = set(eachsummoned) & set(r_pool)
        rsummoned = list(rsummoned)
        rsummoned.sort()
        msummoned = set(eachsummoned) & set(m_pool)
        msummoned = list(msummoned)
        msummoned.sort()
        if ur >= 1:
            print("URs summoned:")
            for uc in range(len(ursummoned)):
                print(" You summoned " + str(summoned.count(ursummoned[uc])) + " of " + str(ursummoned[uc]))
        if sr >= 1:
            print("SRs summoned:")
            for sc in range(len(srsummoned)):
                print(" You summoned " + str(summoned.count(srsummoned[sc])) + " of " + str(srsummoned[sc]))
        if r >= 1:
            print("Rs summoned:")
            for rc in range(len(rsummoned)):
                print(" You summoned " + str(summoned.count(rsummoned[rc])) + " of " + str(rsummoned[rc]))
        if m >= 1:
            print("Ms summoned:")
            for mc in range(len(msummoned)):
                print(" You summoned " + str(summoned.count(msummoned[mc])) + " of " + str(msummoned[mc]))
        print("Statistics\n~~~~~~~~~~~~~~~~~~")
        print("You summoned " + str(ur) + " URs in total")
        print("You summoned " + str(sr) + " SRs in total")
        print("You summoned " + str(r) + " Rs in total")
        print("You summoned " + str(m) + " Ms in total")
        print("To summon " + str(summons) + " amount of times, you will have to spend " + str(summons*150) + " Soul Embers or " + str(summons*100) + " Crystals.")
        summoned = []
        eachsummoned = []
        ur = 0
        sr = 0
        r = 0
        m = 0
        while ag != 2:
            again = input("Would you like to summon again?\nAnswer (Yes/No): ")
            if again == "Yes":
                ag = 2
                yes = 1
            elif again == "No":
                ag = 2
                yes = 2
                print("See you later, fellow Master Attendant!")
                time.sleep(3)
            else:
                print("That is not a valid answer. Please try again.")
                time.sleep(1)
