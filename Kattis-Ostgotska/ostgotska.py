sentence = list(input().split(' '))

ae = len([x for x in sentence if "ae" in x])

proc = ae/len(sentence)

if proc>=.4:
    print("dae ae ju traeligt va") 
else: 
    print("haer talar vi rikssvenska")