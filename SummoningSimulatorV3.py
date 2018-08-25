import random
import time
summon_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop", "Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake", "Skewer", "Jello", "Pancake", "Popcorn", "Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
ur_pool = ["Crab Long Bao", "Foie Gras", "Peking Duck", "B-52", "Bamboo Rice", "Gingerbread", "Boston Lobster", "Double Scoop"]
sr_pool = ["Tiraumisu", "Escargot", "Hotdog", "Mango Pudding", "Hamburger", "Steak", "Tangyuan", "Sanma", "Napoleon Cake", "Salad", "Pastel de nata", "Yuxiang", "Sukiyaki", "Brownie", "Red Wine", "Gyoza", "Chocolate", "Eggette", "Pineapple Cake"]
r_pool = ["Long Bao", "Coffee", "Sashimi", "Macaron", "Zongzi", "Sakuramochi", "Tom Yum", "Taiyaki", "Milk", "Dorayaki", "Sake", "Tempura", "Spicy Gluten", "Jiuniang", "Omurice", "Orange Juice", "Ume Ochazuke", "Miso Soup", "Yellow Wine"]
m_pool = ["Skewer", "Jello", "Pancake", "Popcorn"]
rarity_pool = ["M", "R", "SR", "UR"]
roll = []
previous = []
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
lsummon_pool = [items.lower() for items in summon_pool]
lrarity_pool = [itemr.lower() for itemr in rarity_pool]
option = "Pick an option an enter the appropriate number\n\
Summon:\n\
1. Once\n\
2. 6 times\n\
3. 1000 times\n\
4. As much as desired\n\
5. For a specific food soul\n\
6. For a specific rarity\n\
Leave your answer blank to repeat last action\n\
~~~~~~~~~~~~~\n\
Answer: "
time.sleep(1)
print("Made by Master Attendant Dylan. UID: 104209")
time.sleep(2)
print("Welcome, fellow Master Attendant!")
time.sleep(2)
print("This is a simulator on summoning food souls!")
time.sleep(2)
print("Please note that this is only a simulator and summons in here will NOT affect your in-game experience.")
time.sleep(2)
choice = input(option)
while yes != 2:
    ag = 0
    summoned = []
    eachsummoned = []
    summons = 0
    ur = 0
    sr = 0
    r = 0
    m = 0
    if choice == "1" or choice == "2" or choice == "3":
        if choice == "1":
            summons = 1
        elif choice == "2":
            summons = 6
        elif choice == "3":
            summons == 1000
        print("Redirecting you to option...")
        time.sleep(1)
        print("Summoning food soul...")
        time.sleep(5)
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
    elif choice == "4":
        c1 = 0
        print("Redirecting you to option...")
        time.sleep(1)
        while c1 != 1:
            summons = input("Enter the amount of times you want to summon: ")
            if not(summons.isdigit()):
                print("Error - Invalid input: Must be a positive integer")
            elif int(summons) <= 0:
                print("Error - Invalid number: Must be more than 0")
            elif int(summons) >= 1:
                c1 = 1
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
    elif choice == "5":
        c2 = 0
        print("Redirecting you to option...")
        time.sleep(1)
        while c2 != 1:
            want_foodsoul = input("Enter food soul you want to summon: ")
            lwant_foodsoul = want_foodsoul.lower()
            if lwant_foodsoul not in lsummon_pool:
                print("Error - Invalid input: Food Soul does not exsist or improper spelling")
            elif lwant_foodsoul in lsummon_pool:
                c2 = 1
                c21 = 0
                while c21 != 1:
                    amount = input("Enter how many of the desired food soul you want to summon: ")
                    if not(amount.isdigit()):
                        print("Error - Invalid input: Must be a positive integer")
                    elif int(amount) <= 0:
                        print("Error - Invalid number: Must be more than 0")
                    elif int(amount) >= 1:
                        c21 = 1
                        print("Summoning food souls...\n")
                        time.sleep(5)
                        count_foodsoul = 0
                        while int(amount) != count_foodsoul:
                            foodsoul = random.choice(roll)
                            lfoodsoul = foodsoul.lower()
                            summoned += [foodsoul, ]
                            if foodsoul in ur_pool:
                                ur += 1
                                summons += 1
                            if lwant_foodsoul == lfoodsoul:
                                count_foodsoul += 1
                                if int(amount) < 100:
                                    if summons == 1:
                                        print("~ You summoned 1 " + foodsoul + "after 1 summon.")
                                    else:
                                        print("~ You summoned " + str(count_foodsoul) + " " + foodsoul + " after " + str(summons) + " summons.")
                            elif foodsoul in sr_pool:
                                sr += 1
                                summons += 1
                            elif foodsoul in r_pool:
                                r += 1
                                summons += 1
                            elif foodsoul in m_pool:
                                m += 1
                                summons += 1
    elif choice == "6":
        c3 = 0
        print("Redirecting you to option...")
        time.sleep(1)
        while c3 != 1:
            want_rarity = input("Enter rarity you want to summon (M/R/SR/UR): ")
            lwant_rarity = want_rarity.lower()
            if lwant_rarity not in lrarity_pool:
                print("Error - Invalid input: Rarity does not exsist or improper spelling")
            elif lwant_rarity in lrarity_pool:
                c3 = 1
                c31 = 0
                while c31 != 1:
                    amountr = input("Enter how many of the desired rarity you want to summon: ")
                    if not(amountr.isdigit()):
                        print("Error - Invalid input: Must be a positive integer")
                    elif int(amountr) <= 0:
                        print("Error - Invalid number: Must be more than 0")
                    elif int(amountr) >= 1:
                        c31 = 1
                        print("Summoning food souls...\n")
                        time.sleep(5)
                        foodsoul = ""
                        count_foodsoul = 0
                        while int(amountr) != count_foodsoul:
                            foodsoul = random.choice(roll)
                            summoned += [foodsoul, ]
                            if foodsoul in ur_pool:
                                ur += 1
                                summons += 1
                                if lwant_rarity == "ur":
                                    count_foodsoul += 1
                                    if int(amountr) > 100:
                                        if summons == 1:
                                            print("~ You summoned a UR " + foodsoul + "after 1 summon.")
                                        else:
                                            print("~ You summoned a UR " + foodsoul + " after " + str(summons) + " summons.")
                            elif foodsoul in sr_pool:
                                sr += 1
                                summons += 1
                                if lwant_rarity == "sr":
                                    count_foodsoul += 1
                                    if int(amountr) > 100:
                                        if summons == 1:
                                            print("~ You summoned a SR " + foodsoul + "after 1 summon.")
                                        else:
                                            print("~ You summoned a SR " + foodsoul + " after " + str(summons) + " summons.")
                            elif foodsoul in r_pool:
                                r += 1
                                summons += 1
                                if lwant_rarity == "r":
                                    count_foodsoul += 1
                                    if int(amountr) > 100:
                                        if summons == 1:
                                            print("~ You summoned a R " + foodsoul + "after 1 summon.")
                                        else:
                                            print("~ You summoned a R " + foodsoul + " after " + str(summons) + " summons.")
                            elif foodsoul in m_pool:
                                m += 1
                                summons += 1
                                if lwant_rarity == "m":
                                    count_foodsoul += 1
                                    if int(amountr) > 100:
                                        if summons == 1:
                                            print("~ You summoned a M " + foodsoul + "after 1 summon.")
                                        else:
                                            print("~ You summoned a M " + foodsoul + " after " + str(summons) + " summons.")
    elif choice == "":
        if previous == []:
            print("Error - No previous action")
            time.sleep(1)
            choice = input(option)
        else:
            if previous[0] == "1" or previous[0] == "2" or previous[0] == "3" or previous[0] == "4":
                choice = previous[0]
                summons = previous[1]
                print("Redirecting you to option...")
                time.sleep(1)
                print("Summoning food soul...")
                time.sleep(5)
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
            elif previous[0] == "5":
                print("Redirecting you to option...")
                time.sleep(1)
                choice = previous[0]
                lwant_foodsoul = previous[1]
                amount = previous[2]
                print("Summoning food souls...\n")
                time.sleep(5)
                count_foodsoul = 0
                while int(amount) != count_foodsoul:
                    foodsoul = random.choice(roll)
                    lfoodsoul = foodsoul.lower()
                    summoned += [foodsoul, ]
                    if foodsoul in ur_pool:
                        ur += 1
                        summons += 1
                    if lwant_foodsoul == lfoodsoul:
                        count_foodsoul += 1
                        if int(amount) > 100:
                            if summons == 1:
                                print("~ You summoned 1 " + foodsoul + "after 1 summon.")
                            else:
                                print("~ You summoned " + str(count_foodsoul) + " " + foodsoul + " after " + str(summons) + " summons.")
                    elif foodsoul in sr_pool:
                        sr += 1
                        summons += 1
                    elif foodsoul in r_pool:
                        r += 1
                        summons += 1
                    elif foodsoul in m_pool:
                        m += 1
                        summons += 1
            elif previous[0] == "6":
                c3 = 0
                print("Redirecting you to option...")
                time.sleep(1)
                choice = previous[0]
                lwant_rarity = previous[1]
                amountr = previous[2]
                print("Summoning food souls...\n")
                time.sleep(5)
                foodsoul = ""
                count_foodsoul = 0
                while int(amountr) != count_foodsoul:
                    foodsoul = random.choice(roll)
                    summoned += [foodsoul, ]
                    if foodsoul in ur_pool:
                        ur += 1
                        summons += 1
                        if lwant_rarity == "ur":
                            count_foodsoul += 1
                            if int(amountr) > 100:
                                if summons == 1:
                                    print("~ You summoned a UR " + foodsoul + "after 1 summon.")
                                else:
                                    print("~ You summoned a UR " + foodsoul + " after " + str(summons) + " summons.")
                    elif foodsoul in sr_pool:
                        sr += 1
                        summons += 1
                        if lwant_rarity == "sr":
                            count_foodsoul += 1
                            if int(amountr) > 100:
                                if summons == 1:
                                    print("~ You summoned a SR " + foodsoul + "after 1 summon.")
                                else:
                                    print("~ You summoned a SR " + foodsoul + " after " + str(summons) + " summons.")
                    elif foodsoul in r_pool:
                        r += 1
                        summons += 1
                        if lwant_rarity == "r":
                            count_foodsoul += 1
                            if int(amountr) > 100:
                                if summons == 1:
                                    print("~ You summoned a R " + foodsoul + "after 1 summon.")
                                else:
                                    print("~ You summoned a R " + foodsoul + " after " + str(summons) + " summons.")
                    elif foodsoul in m_pool:
                        m += 1
                        summons += 1
                        if lwant_rarity == "m":
                            count_foodsoul += 1
                            if int(amountr) > 100:
                                if summons == 1:
                                    print("~ You summoned a M " + foodsoul + "after 1 summon.")
                                else:
                                    print("~ You summoned a M " + foodsoul + " after " + str(summons) + " summons.")
    else:
        print("Error - Option not available")
        time.sleep(1)
        choice = input(option)
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
        print("\nURs summoned:")
        for uc in range(len(ursummoned)):
            print(" You summoned " + str(summoned.count(ursummoned[uc])) + " of " + str(ursummoned[uc]))
    if sr >= 1:
        print("\nSRs summoned:")
        for sc in range(len(srsummoned)):
            print(" You summoned " + str(summoned.count(srsummoned[sc])) + " of " + str(srsummoned[sc]))
    if r >= 1:
        print("\nRs summoned:")
        for rc in range(len(rsummoned)):
            print(" You summoned " + str(summoned.count(rsummoned[rc])) + " of " + str(rsummoned[rc]))
    if m >= 1:
        print("\nMs summoned:")
        for mc in range(len(msummoned)):
            print(" You summoned " + str(summoned.count(msummoned[mc])) + " of " + str(msummoned[mc]))
    if summons >= 1:
        print("\nStatistics\n~~~~~~~~~~~~~~~~~~")
        print("You summoned " + str(ur) + " URs in total, that is " + str(round((ur/summons)*100, 2)) + "% of summons.")
        print("You summoned " + str(sr) + " SRs in total, that is " + str(round((sr/summons)*100, 2)) + "% of summons.")
        print("You summoned " + str(r) + " Rs in total, that is " + str(round((r/summons)*100, 2)) + "% of summons.")
        print("You summoned " + str(m) + " Ms in total, that is " + str(round((m/summons)*100, 2)) + "% of summons.")
        print("\nTo summon " + str(summons) + " amount of times, you will have to spend " + str(summons*150) + " Soul Embers or " + str(summons*100) + " Crystals.")
        if choice == "5":
            previous = [choice, lwant_foodsoul, amount]
        elif choice == "6":
            previous = [choice, lwant_rarity, amountr]
        else:
            previous = [choice, summons]
        while ag != 2:
            again = input("\nWould you like to use the simulator again?\nAnswer (Yes/No): ")
            lagain = again.lower()
            if lagain == "yes":
                ag = 2
                yes = 1
                choice = input(option)
            elif lagain == "no":
                ag = 2
                yes = 2
                print("See you later, fellow Master Attendant!")
                time.sleep(3)
            else:
                print("That is not a valid answer. Please try again.")
                time.sleep(1)
