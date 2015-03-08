from collections import defaultdict

class Problem:
    def sortHand(self, hand):
        sortedHand = [hand[0]]
        for i in range(1, 5):
            rank = int(self.getRankOfCard(hand[i][0]))
            k = 0
            while k < len(sortedHand) and int(self.getRankOfCard(sortedHand[k][0])) < rank:
                k = k + 1
            sortedHand.insert(k, hand[i])
        return sortedHand
            
    def getRankOfCard(self, card):
        rank = card[0]
        if rank == 'A':
            return '14'
        if rank == 'K':
            return '13'
        if rank == 'Q':
            return '12'
        if rank == 'J':
            return '11'
        if rank == 'T':
            return '10'
        return '0' + rank
        
    def hasFlush(self, hand):
        suit = hand[0][1]
        for card in hand:
            if card[1] != suit:
                return False
        return True
        
    def hasStraight(self, hand):
        expectedRank = int(self.getRankOfCard(hand[0][0]))
        for card in hand:
            if int(self.getRankOfCard(card[0])) != expectedRank:
                return False
            expectedRank = expectedRank + 1
        return True
    
    def lookForFullHouse(self, hand):
        has3, rank = self.lookFor3(hand)
        if has3:
            if hand[0][0] == hand[2][0]:
                if hand[3][0] == hand[4][0]:
                    return True, rank
            if hand[2][0] == hand[4][0]:
                if hand[0][0] == hand[1][0]:
                    return True, rank
            if hand[0][0] == hand[4][0]:
                return True, rank
        return False, ""
                
    
    def lookFor4(self, hand):
        if hand[0][0] == hand[1][0] == hand[2][0] == hand[3][0]:
            return True, self.getRankOfCard(hand[0]) + self.getRankOfCard(hand[4])
        if hand[1][0] == hand[2][0] == hand[3][0] == hand[4][0]:
            return True, self.getRankOfCard(hand[4]) + self.getRankOfCard(hand[0])
        return False, ""

    def lookFor3(self, hand):
        maxCount = 0
        count = 1
        previousCard = hand[0]
        for i in range(1, 5):
            if previousCard[0] == hand[i][0]:
                count = count + 1
            else:
                count = 1
            maxCount = max(maxCount, count)
            previousCard = hand[i]
        if maxCount != 3:
            return False, ""
        if hand[0][0] == hand[2][0]: # 3 are at start
            return True, self.getRankOfCard(hand[0]) + self.getRankOfCard(hand[4]) + self.getRankOfCard(hand[3])
        elif hand[2][0] == hand[4][0]: # 3 are at end
            return True, self.getRankOfCard(hand[4]) + self.getRankOfCard(hand[1]) + self.getRankOfCard(hand[0])
        return True, self.getRankOfCard(hand[2]) + self.getRankOfCard(hand[4]) + self.getRankOfCard(hand[0])
        
    def findIndexOfFirstPair(self, hand):
        previousCard = hand[0]
        for i in range(1, len(hand)):
            if previousCard[0] == hand[i][0]:
                if i == len(hand) - 1 or hand[i] != hand[i + 1]:
                    return i - 1
            previousCard = hand[i]
        return -1
                        
    def lookFor2Twos(self, hand):
        firstIndex = self.findIndexOfFirstPair(hand)
        if firstIndex == -1:
            return False, ""
        nextSearchIndex = firstIndex + 2
        if len(hand[nextSearchIndex:]) < 2:
            return False, ""
        secondIndex = self.findIndexOfFirstPair(hand[nextSearchIndex:])
        if secondIndex == -1:
            return False, ""
        secondIndex = secondIndex + nextSearchIndex
        rank = self.getRankOfCard(hand[secondIndex]) + self.getRankOfCard(hand[firstIndex])
        if firstIndex == 0:
            if secondIndex == 2:
                return True, rank + self.getRankOfCard(hand[4])
            return True, rank + self.getRankOfCard(hand[2])
        return True, rank + self.getRankOfCard(hand[0])

    def lookFor2(self, hand):
        index = self.findIndexOfFirstPair(hand)
        if index == -1:
            return False, ""
        rank = self.getRankOfCard(hand[index])
        indexes = [i for i in range(0, 5)]
        indexes.remove(index)
        indexes.remove(index + 1)
        indexes.reverse()
        for i in indexes:
            rank = rank + self.getRankOfCard(hand[i])
        return True, rank
        
    def getRank(self, hand):
        # Expects hand to be sorted from worst to best card...
        if self.hasFlush(hand) and self.hasStraight(hand):
            return '8.' + self.getRankOfCard(hand[4])  # Append rank of highest card
        has4, rank = self.lookFor4(hand)
        if has4:
            return '7.' + rank
        hasFullHouse, rank = self.lookForFullHouse(hand)
        if hasFullHouse:
            return '6.' + rank
        if self.hasFlush(hand):
            return '5.' + self.getRankOfCard(hand[4])
        if self.hasStraight(hand):
            return '4.' + self.getRankOfCard(hand[4])
        has3, rank = self.lookFor3(hand)
        if has3:
            return '3.' + rank
        has2Twos, rank = self.lookFor2Twos(hand)
        if has2Twos:
            return '2.' + rank
        has2, rank = self.lookFor2(hand)
        if has2:
            return '1.' + rank
        return '0.' + self.getRankOfCard(hand[4]) + self.getRankOfCard(hand[3]) + self.getRankOfCard(hand[2]) + self.getRankOfCard(hand[1]) + self.getRankOfCard(hand[0])
        
        
    def run(self):
        #print(self.getRank(['3C','4C','5C','6C','8C']))
        #return
        
        player1wins = 0
        file = open('../54.txt')
        handsChecked = 0
        while True:
            line = file.readline()
            if len(line) == 0:
                print('Checked number of hands: ' + str(handsChecked))
                print(player1wins)
                return
            cards = line.split(' ')
            player1hand = self.sortHand(cards[:5])
            player2hand = self.sortHand(cards[5:])
            #print('Player1 hand: ' + ','.join(player1hand))
            #print('Player2 hand: ' + ','.join(player2hand))

            rank1 = self.getRank(player1hand)
            rank2 = self.getRank(player2hand)
            #print('Player1 hand: ' + ','.join(player1hand) + ' rank: ' + rank1)
            #print('Player2 hand: ' + ','.join(player2hand) + ' rank: ' + rank2)
            if rank1 > rank2:
                print('Player 1 wins a hand!')
                player1wins = player1wins + 1
            elif rank1 == rank2:
                    print('OOPS! DRAW!')
            handsChecked = handsChecked + 1
            print('At Hand: ' + str(handsChecked))


if __name__ == '__main__':
    solver = Problem()
    solver.run()