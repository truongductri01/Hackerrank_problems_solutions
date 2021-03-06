# Link: https://www.hackerrank.com/challenges/the-minion-game/problem


Game_Rule = '''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
1. Both players are given the same string, S.
2. Both players have to make substrings using the letters of the string S.
3. Stuart has to make words starting with consonants.
4. Kevin has to make words starting with vowels.
5. The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S.'''

Idea = '''
    We calculate the total points possible to gain from the string.        
        Total point possible for any given string is a sum of:
        1. Points form by every single character in the string (aka. length of the string)
        2. Points form by string between every 2 characters 
        (like calculate the total segments of a line between every 2 points) 
        
        For example:
        If the string is BANANA has length = 6
        1. points form by single characters = 6
        2. points form by segments: 6*(6-1)/2 pairs. The formula to calculate pairs.
    Then we just have to calculate a score for one person 'cause the other's score is total - one's.
    So we choose to calculate Stuart's points.
        We just need to locate the consonants, we do not have to count the occurrence anymore.
        BANANA:
            The first consonant is B, it can form 6 diff. words.
                B
                BA
                BAN
                BANA
                BANAN
                BANANA
                It is just equal to length of BANANA - the index of B.
                    N
                    NA
                    NAN
                    NANA
                    equal to length of BANANA(6) - index of N (2) = 4 
                And so on ...
        '''

Testing = '''
BANANA -> Stuart 12

BAANANAS -> Kevin 19

NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN
-> Stuart 7501500
'''


def is_vowel(char):
    vowels_array = ['A', 'E', 'O', 'U', 'I']
    if char in vowels_array:
        return True
    else:
        return False


def total_score(string):
    length = len(string)
    single_character_point = length
    long_string_points = (length * (length - 1)) // 2
    total = single_character_point + long_string_points
    return total


def stuart_point(string):
    stuart = 0
    for i in range(len(string)):
        char = string[i]
        if is_vowel(char):
            continue
        else:
            # print("Point before:", stuart)
            # print(char)
            stuart += len(string) - i
            # print("Point after:", stuart)
            # print()
    return stuart


def minion_game(string):
    stuart = stuart_point(string)
    kevin = total_score(string) - stuart
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == "__main__":
    f = open("Input")
    for x in f:
        string_to_play = x.rstrip()
        print(string_to_play)
        minion_game(string_to_play)
    f.close()
