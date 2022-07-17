import random

def heads_tails(number_of_flips):
    
    tails_count = 0
    heads_count = 0
    
    for i in range(number_of_flips):
        
        rand = random.randint(1,2)
        
        if rand == 1:
            tails_count += 1
            
            print(tails_count, 'tails')
    
        else:
            heads_count += 1
            
            print(heads_count, 'heads')
    
    print('tails', tails_count)
    print('heads', heads_count)
    

heads_tails(823651)