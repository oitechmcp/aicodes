# 16. FOPL
from itertools import product as iproduct

def fopl():
    domain = ['Alice','Bob','Charlie']
    likes  = {('Alice','Bob'),('Bob','Charlie'),('Alice','Charlie')}
    mortal = {x for x in domain}

    human_likes = lambda x,y: (x,y) in likes
    is_mortal   = lambda x: x in mortal

    print("All humans are mortal:", all(is_mortal(x) for x in domain))
    print("Someone likes Bob:", any(human_likes(x,'Bob') for x in domain))
    print("Alice likes someone:", any(human_likes('Alice',y) for y in domain))
    print("Likes relation:", [(x,y) for x,y in iproduct(domain,domain) if human_likes(x,y)])

fopl()