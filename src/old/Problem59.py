from collections import defaultdict

class Problem:
    def xor(self, a, b):
        return a ^ b
        
    def run(self):
        file = open('../59.txt')
        chars = file.read().split(',')
        original = list(chars)
        counts1 = defaultdict(int)
        counts2 = defaultdict(int)
        counts3 = defaultdict(int)
        while len(chars) > 2:
            char = chars.pop()
            counts1[char] = counts1[char] + 1
            char = chars.pop()
            counts2[char] = counts2[char] + 1
            char = chars.pop()
            counts3[char] = counts3[char] + 1
        counts1[chars[0]] = counts1[chars[0]] + 1

        plainText = []
        # PASSWORD is 'gdo'
        while len(original) > 2:
            plainText.append(chr(int(original.pop()) ^ 103))
            plainText.append(chr(int(original.pop()) ^ 100))
            plainText.append(chr(int(original.pop()) ^ 111))
        plainText.append(chr(int(original.pop()) ^ 103))
            
        print(len(original))
        plainText.reverse()
        print(''.join(plainText))
        sum = 0
        for char in plainText:
            sum = sum + ord(char)
        print(sum)
        


if __name__ == '__main__':
    solver = Problem()
    solver.run()