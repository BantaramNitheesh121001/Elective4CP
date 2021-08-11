# This is the most complicated part. Write the function playstep2(hand, dice) that plays step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finally a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this way,
# we'd probably use a random-number generator.

# With that, the function plays step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(playstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it already is. Finally, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(playstep2(544, 456) == (644, 45))
# If you have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure you carefully understand them:
# assert(playstep2(413, 2312) == (421, 23))
# assert(playstep2(413, 2345) == (544, 23))
# assert(playstep2(544, 23) == (443, 2))
# assert(playstep2(544, 456) == (644, 45))
# Hint: You may wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, you may wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.

def dicetoorderedhand(a, b, c):
    	# your code goes here
	val = (a,b,c)
	mx = max(val)
	mn = min(val)
	left = a + b + c - mn - mx
	return mx*10**(2)+left*10+mn

def handtodice(hand):
    	# your code goes here
	hand = str(hand)
	val = list()
	for i in hand:
    		val.append(int(i))
	return tuple(val)

def checkmatch(hand):
    d1 = hand[0]
    d2 = hand[1]
    d3 = hand[2]
    if d1 == d2:
        return d1,d2
    elif d2 == d3:
        return d2,d3
    elif d1 == d3:
        return d1,d3

def playstep2(hand, dice):
    hand = handtodice(hand)
    if checkmatch(hand):
        hand = checkmatch(hand)
        future = dice%10
        dice = dice//10
        hand = dicetoorderedhand(hand[0],hand[1],future)
        return hand,dice
    hand = max(hand)
    future = dice%100
    dice = dice // 100
    hand = future * 10 + hand
    hand = handtodice(hand)
    return dicetoorderedhand(hand[0],hand[1],hand[2]), dice
print(playstep2(413, 2312))