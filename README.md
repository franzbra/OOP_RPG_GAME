# OOP_RPG_GAME

A role playing game where you have to build and feed a prehistoric tribe during the stone age. 

## To do: ##
### Characters ###
- [x] add communication/intelligence stats to characters
- [x] add animal affinity
- [ ] add moral 
- [x] add weapon mastery value. This should increase everytime we manage to hit a monster
- [x] add crafting skills (this is valid both for building statues, draw paintings or constructing tools)
- [x] Test crafting procedure, the inventory of the tribe should be updated consistently
- [x] implement a dynamic to craft tools based on your tribe resources
- [ ] put a limit to the number of hours character can train or gather resources or number of pf you gain by sleeping
- [x] actions consume pf


### Chatbot ### 
- [ ] If new characters are evil, they will steal items from the tribe, attack or curse them(depending on their class)
- [x] If the communication/intelligence of the bot is lower than yours, you could try to invite him to join your tribe. 

### Monsters ### 
- [x] Add dexterity
- [x] if a character has a value of animal affinity larger than some treshold, the monster can be tamed.
- [ ] Add two kind of monsters: regular or legendary. Chances to find a legendary monster are 10%

### Combat system ### 
- [x] Modify combat system. Add a chance to miss the target based on its dexterity
- [x] Modify combat system. It should be turn-based. Monster can strike back!
- [ ] The monster can try to escape if its total defense is smaller than cumulative attack of the tribe
- [ ] Add the possibility to perform critical attacks (if the attack stat is larger than some threshold, the damage is doubled)

### Prayers ###
- [x] Add to possibility to pray obtaining more chance to find meat, items ecc

### Time ###
- [x] Implement a way to simulate the passing of time: every 10 rounds a day goes by
- [ ] Give the player a mission to complete
### Tribe ### 
- [x] Create a Tribe class
- [ ] While exploring, new random tribes could appear. You might interact with their leader to exchange items or try to steal their goods. To do that, introduce a stealth stats in the characters
- [ ] Dolls, tends, paintings and other stuff should add prestige to your tribe, making other character more eager to join you.
- [ ] Magical objects give extra chance to find meat, items ecc when praying
- [x] Create an inventory for the tribe with meat, bones, wood, ...
- [x] Fix monster in the tribe: their meat and bones are not available!
- [x] Each night the tribe has to eat. Those who don't eat die.
- [ ] Implement the possibility to hunt and gather resources with all the members of the tribe. Different members should also be able to do different activities
