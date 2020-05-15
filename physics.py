from particle import*

def collision(p1, p2): #particles as parameters
    p1.vel_v , p2.vel_v = p2.vel_v , p1.vel_v
    p1.vel_h , p2.vel_h = p2.vel_h , p1.vel_h
