 # more advanced AI for TT
 
 def ai_move():

 # Then checks to see whether it can prevent a loss (24 possibilities)
        # Across first
        if myboard['top-r'] == 'x' and myboard ['top-m']  == 'x' and myboard['top-l'] != 'o':
            myboard ['top-l '] = 'o'
        elif myboard['mid-r'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['mid-l'] != 'o':
            myboard ['mid-l '] = 'o'
        elif myboard['bottom-r'] == 'x' and myboard ['bottom-m'] == 'x'\
            and myboard['bottom-l'] != '0':
            myboard ['bottom-l '] = 'o'
            #Im up to here....changing to != 'o'
        elif myboard['top-l'] == 'x' and myboard ['top-m'] == 'x'\
            and myboard['top-r'] == ' ':
            myboard ['top-r '] = 'o'
        elif myboard['mid-l'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['mid-r'] == ' ':
            myboard ['mid-r '] = 'o'
        elif myboard['bottom-l'] == 'x' and myboard ['bottom-m'] == 'x'\
            and myboard['bottom-r'] == ' ':
            myboard ['bottom-r'] = 'o'
        elif myboard['bottom-l'] == 'x' and myboard ['bottom-r'] == 'x'\
            and myboard['bottom-m'] == ' ':
            myboard ['bottom-m'] = 'o'
        elif myboard['top-r'] == 'x' and myboard ['top-l'] == 'x'\
            and myboard['top-m'] == ' ':
            myboard ['top-m '] = 'o'
        elif myboard['mid-r'] == 'x' and myboard ['mid-l'] == 'x'\
            and myboard['mid-m'] == ' ':
            myboard ['mid-m '] = 'o'
        # Now the up and down - dont forget all the combos
        elif myboard['top-r'] == 'x' and myboard ['mid-r'] == 'x'\
            and myboard['bottom-r'] == ' ':
            myboard ['bottom-r '] = 'o'
        elif myboard['bottom-r'] == 'x' and myboard ['mid-r'] == 'x'\
            and myboard['top-r'] == ' ':
            myboard ['top-r '] = 'o'
    
        elif myboard['top-r'] == 'x' and myboard ['bottom-r'] == 'x'\
            and myboard['mid-r'] == ' ':
            myboard ['mid-r '] = 'o' 
        elif myboard['top-m'] == 'x' and myboard ['bottom-m'] == 'x'\
            and myboard['mid-m'] == ' ':
            myboard ['mid-m '] = 'o'
        elif myboard['top-m'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['bottom-m'] == ' ':
            myboard ['bottom-m'] = 'o'
        elif myboard['bottom-m'] == 'x' and myboard ['mid-m'] == 'x'\
         and myboard['top-m'] == ' ':
            myboard ['top-m'] = 'o'
        elif myboard['top-l'] == 'x' and myboard ['bottom-l'] == 'x'\
            and myboard['mid-l'] == ' ':
            myboard ['mid-l '] = 'o'
        elif myboard['bottom-l'] == 'x' and myboard ['mid-l'] == 'x'\
            and myboard['top-l'] == ' ':
            myboard ['top-l'] = 'o'
        elif myboard['top-l'] == 'x' and myboard ['mid-l'] == 'x'\
            and myboard['bottom-l'] == ' ':
            myboard ['bottom-l'] = 'o'
        # Now diagonal (6 possibilities)
        elif myboard['top-r'] == 'x' and myboard ['bottom-l'] == 'x'\
            and myboard['mid-m'] == ' ':
            myboard ['mid-m '] = 'o'
        elif myboard['top-l'] == 'x' and myboard ['bottom-r'] == 'x'\
            and myboard['mid-m'] == ' ':
            myboard ['mid-m'] = 'o'
        elif myboard['top-r'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['bottom-l'] == ' ':
            myboard ['bottom-l'] = 'o'
        elif myboard['top-l'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['bottom-r'] == ' ':
            myboard ['bottom-r'] = 'o'
        elif myboard['bottom-l'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['top-r'] == ' ':
            myboard ['top-r '] = 'o'
        elif myboard['bottom-r'] == 'x' and myboard ['mid-m'] == 'x'\
            and myboard['top-l'] == ' ':
            myboard ['top-l'] = 'o'