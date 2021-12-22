import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# set conf
Nr = 20 # rows number
Nc = 20 # columns number
n = 3 # seed matrix dimension (nxn)
S = 10 # number of seeds
G = 100 # number of generations
st = 'rand'


def initialize_grid():
    global n
    universe = np.zeros((Nr, Nc))
    for s in range(S):
        if st == 'rand':
            seed = np.random.randint(2, size=(n, n))
        elif st == 'glider':
            seed = np.array([
                             [0, 1, 0],
                             [0, 0, 1],
                             [1, 1, 1]
                            ])
            n = 3
        x = np.random.randint(Nr)
        y = np.random.randint(Nc)
        X = x%Nr
        Y = y%Nc
        try:
            universe[X:X+n, Y:Y+n] = seed
            print(st, ' seed: ',s,' IN at position: ',X,Y)
        except:
            print(st, ' seed: ',s,' OUT at position: ',X,Y)
    return universe    

    return universe

def cell_check(A):
    newA = A.copy()
    for i in range(Nr):
        for j in range(Nc):
            tot = int(A[(i-1)%Nr,(j-1)%Nc] + A[i,(j-1)%Nc] + A[(i+1)%Nr,(j-1)%Nc] + 
                      A[(i-1)%Nr, j] + A[(i+1)%Nr, j] +
                      A[(i-1)%Nr, (j+1)%Nc] + A[i, (j+1)%Nc] + A[(i+1)%Nr,(j+1)%Nc])

            # apply Conway's rules
            if A[i, j]  == 1:
                if (tot < 2) or (tot > 3):
                    newA[i, j] = 0
            else:
                if tot == 3:
                    newA[i, j] = 1
    return newA


def main():
    grid = initialize_grid()

    fig = plt.figure()
    plt.axis('off')
    ims = []

    for g in range(G+1):
        print("Generation: ", g)
        newgrid = cell_check(grid)
        ims.append((plt.imshow(newgrid, cmap='binary'),))
        grid[:] = newgrid[:]

    im_ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True)
    im_ani.save(st+'_conway.gif', writer="imagemagick")


# call main 
if __name__ == '__main__': 
        main() 
