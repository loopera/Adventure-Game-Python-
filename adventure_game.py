# ADVENTURE GAME

answer = input('You are going on a treasure hunt in a tropical island and found a boat. Do you want to get on the boat? Type YES or NO: ')

# SCENARIO YES PART 1
if answer.lower() == ('yes'):

    # SCENARIO YES PART 2A
    food = input('\nYou are now in the boat and then suddenly there is a shark swimming next to the boat? You decided to feed the shark so it will go away after. You found a fish and a carrot in the boat. What will you feed the shark? FISH or CARROT?: ')
    if food.lower() == ('fish'):
        action = input('\nYou threw the fish towards the shark. However, this shark is apparently vegan and refused to eat it. The shark got offended and started to slam its body on to the boat, which is now on the brink of capsizing. What will you do? PRAY, FEED the carrot, or SHOUT for help? Type PRAY, FEED, or SHOUT for your answer: ')

# SCENARIO YES PART 3A
        if action.lower() == ('pray'):
            print('\nYou decided to pray and suddenly a miracle happened. Another boat passed by and rescued you. Congratulations!')
        elif action.lower() == ('feed'):
            print(
                '\nThe shark ate the carrot and the happy vegan shark swam away from the boat. You survived!')
        elif action.lower() == ('shout'):
            print('\nYou shouted for help, which made the shark even angrier. The shark eventually capsized the boat. Luckily, you are an excellent swimmer and you swam as fast as you can to the shore for safety. You made it alive! Phew!')
        else:
            print('\nPlease only answer "PRAY or FEED or SHOUT" to this question. Please go back to the beginning.')

# SCENARIO YES PART 2B
    elif food.lower() == ('carrot'):
        item = input('\nYou threw the carrot to the shark. The shark was so happy because it is apparently a vegan shark. The shark swam away. You looked around the boat and found three items: a BOTTLE, PILLOW, and a MAP. Choose one item: ')

# SCENARIO YES PART 3B
        if item.lower() == ('bottle'):
            print('\nYou grabbed the bottle and noticed something inside. You looked closely and noticed that there is a paper inside. You opened the bottle and found that the paper inside is a map. Congratuations! You have found the treasure map!')
        elif item.lower() == ('pillow'):
            print('\nYou grabbed the pillow and lay your head next to it. You fell asleep. You woke up and realized that everything was just a dream. The End.')
        elif item.lower() == ('map'):
            print('\nYour heart is pounding with excitement and opened the map. Is this the treasure map? You opened the map and found out that there is actually no gold treasure at all in the island. Real treasure comes from the experiences we have in life. The End.')
        else:
            print('\nPlease only answer "BOTTLE, PILLOW, or MAP" to this question. Please go back to the beginning.')
    else:
        print('\nPlease only answer "FISH or CARROT" to this question. Please go back to the beginning.')


# SCENARIO NO PART 1
elif answer.lower() == ('no'):

    # SCENARIO NO PART 2A

    explore = input('\nYou did not go on the boat and decided to explore the island by foot. You found a cave and a forest. Which one will you explore first? CAVE or FOREST?: ')
    if explore.lower() == ('cave'):
        item_2 = input(
            '\nYou went inside the cave and found three items: BOOK, COIN, LAMP. Which item will you pick up? ')

# SCENARIO NO PART 3A
        if item_2.lower() == ('book'):
            print('\nYou picked up the book and found out that this was not an ordinary book. This was the journal of a famous explorer. You read the journal and found out that the real treasure can be found in reading the scriptures. Well done!')
        elif item_2.lower() == ('coin'):
            print('\nYou grabbed the shiny gold coin. You noticed that it was glittering. You got very excited thinking this must be where the treasure is. You bit the gold coin with your teeth to check if it is real gold and found out that it is just a chocolate gold coin. The end.')
        elif item_2.lower() == ('lamp'):
            print('\nYou grabbed the lamp and then you cleaned it with your hand. As you were wiping the lamp, a genie appeared. The genie said he will grant you 3 wishes. Suddenly, something loud is playing in the background. You woke up and noticed that it was your alarm clock. Everything was just a dream. The end.')
        else:
            print(
                '\nPlease only answer "BOOK, COIN or LAMP" to this question. Please go back to the beginning.')

# SCENARIO NO PART 2B
    elif explore.lower() == ('forest'):
        animal = input(
            '\nYou decided to go to the forest and found three animals: RABBIT, COW, and MONKEY. Which animal will you follow? ')
        if animal.lower() == ('rabbit'):
            print('\nYou followed the rabbit and went down into a hole. It was very dark. You turned on your flashlight. You found the secret treasure! The room is full of gold! Congratulations!!!')
        elif animal.lower() == ('cow'):
            print('\nYou followed the cow but the cow kept going deeper and deeper into the forest. Suddenly it was nighttime. You stopped for a bit and fell asleep. Next thing, you opened your eyes and found yourself in your bedroom. You realized that everything was just a dream. The End.')
        elif animal.lower() == ('monkey'):
            print('\nYou followed the monkey as it was climbing and jumping on the trees. The monkey stopped and you found yourself in a beautiful oasis. The view is so beautiful. The beauty of nature is indeed the real treasure. The End.')
        else:
            print('\nPlease only answer "RABBIT, COW or MONKEY" to this question. Please go back to the beginning.')
    else:
        print('\nPlease only answer "CAVE or FOREST" to this question. Please go back to the beginning.')
else:
    print('\nPlease only answer "YES or NO" to this question. Please go back to the beginning.')
    