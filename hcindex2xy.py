# Hilbert curve operators

"""
 B__ __ __ __C
 |           |
 |           |
 |           |
A|__ __ __ __|D
 We could define 12 block operators,d2xy_bc,d2xy_cb,d2xy_ab,
 d2xy_ba,d2xy_ad,d2xy_da,d2xy_cd,d2xy_dc,d2xy_ac,d2xy_ca,
 d2xy_bd,d2xy_db
"""

##---------------d2xy_ab------------------------
def hcindex2xy_ab(n,hcindex):
# n represents the number of point on the axial x/y
    assert(hcindex <= n**2 - 1)
    positions = ([0,0],[1,0],[1,1],[0,1]) #tuple

    #The last two corresponds to which point of posotions
    last2bits     = hcindex & 3
    cor_position  = positions[last2bits]
    x = cor_position[0]
    y = cor_position[1]

    subsuqarebits = hcindex>>2 # cooresponding to the subsuqare
    m = 4 # because the first four points have been given,so start from 4
    while(m <= n):
          m2 = m/2
          case = subsuqarebits & 3 # take the last two bits
    # in the  quadrant named zero,do flip
          if case == 0:
              tmp = x
              x   = y
              y   = tmp
    # in the quadrant named one,do transformation
          elif case == 1:
              x   = x + m2 # keep x unchanged
    # in the quadrant named two,do another transformation
          elif case == 2:
              x  = x + m2
              y  = y + m2
    # in the quadrant named three, do rotation around y=-x and transformation
          elif case == 3:
              temp = y
              y    = m2 -1-x
              x    = m2 -1-temp
              y    = y + m2
    # default case
          else:
              print 'The last2bits:',case,' is not anyone of [0,1,2,3]'
              sys.exit('last2bits error')

          subsuqarebits = subsuqarebits>>2 # case /=4,remove the last two bits
          m   *= 2 # iteration,grow 2 times on one direction
    return x,y
#################################################

#-------------------hcindex2xy_ba------------------------------------
def hcindex2xy_ba(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ab(n,n**2-1-hcindex)
    y   = -y #force the vertex B to be (0,0) by reflecting
    return x,y
########################################################################
#----------------------------------------------------------------------
# ad test failed 2017-03-03  night
# ad test succussful 2017-03-05
def hcindex2xy_ad(n,hcindex):

    assert(hcindex <= n**2 - 1)
    positions = ([0,0],[0,1],[1,1],[1,0]) #tuple

    #The last two corresponds to which point of posotions
    last2bits     = hcindex & 3
    cor_position  = positions[last2bits]
    x = cor_position[0]
    y = cor_position[1]

    subsuqarebits = hcindex>>2 # cooresponding to the subsuqare
    m = 4
    while(m <= n):
         # because the first four points have been given
          m2 = m/2
          case = subsuqarebits & 3 # the last two bits
    # in the  quadrant named zero,do flip
          if case == 0:
             tmp = x
             x   = y
             y   = tmp
    # in the quadrant named one,do transformation
          elif case == 1:
               y   = y + m2 # keep x unchanged
    # in the quadrant named two,do another transformation
          elif case == 2:
               x  = x + m2
               y  = y + m2
    # in the quadrant named three, do rotation around y=-x and transformation
          elif case == 3:
               temp = y
               y    = m2 -1-x
               x    = m2 -1-temp
               x    = x + m2
    # default case
          else:
              print 'The last2bits:',case,' is not anyone of [0,1,2,3]'
              sys.exit('last2bits error')

          subsuqarebits = subsuqarebits>>2 # case /=4,remove the last two bits
          m   *= 2 # iteration,grow 2 times on one direction
    return x,y


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#-------------------hcindex2xy_da-------------------------------------
def hcindex2xy_da(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ad(n,n**2-1-hcindex) # hilbert curve symmetry
# force the vertex D which loacts at (n**2-1,0) in operator hcindex2xy_ad to be (0,0)
    x =x-(n-1)
    return x,y
#####################################################################

 #-------------------hcindex2xy_dc -----------------------------------
def hcindex2xy_dc(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ab(n,hcindex)
    x   = -x # reflect about the axial AB,x = 0
    return x,y
#########################################################################

#------------------hcindex2xy_cd ------------------------------------
def hcindex2xy_cd(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ba(n,hcindex)
    x   = -x # reflection
    return x,y
#########################################################################

#----------------hcindex2xy_bc ---------------------------------------
def hcindex2xy_bc(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ad(n,hcindex)
    y   = -y # reflection
    return x,y
##########################################################################

#---------------hcindex2xy_cb -----------------------------------------
def hcindex2xy_cb(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_da(n,hcindex)
    y   = -y # reflection
    return x,y
#########################################################################

#--------------hcindex2xy_ac ---------------------------------------
def hcindex2xy_ac(n,hcindex):
    assert(hcindex <= n**2 - 1)
    positions = ([0,0],[0,1],[1,0],[1,1]) #tuple


    if n >= 4:
        quart_block = n/2 # 1/4 of the square
        starting_point = ([0,0],[0,quart_block],[quart_block,quart_block-1],[n-1,quart_block])
        ncells_block = quart_block**2
        index_starting = (0,             ncells_block,    2*ncells_block,  3*ncells_block)
        index_ending   = (ncells_block-1,2*ncells_block-1,3*ncells_block-1,4*ncells_block-1)
        if hcindex>=index_starting[0] and hcindex<=index_ending[0]:
            x,y = hcindex2xy_ab(quart_block,hcindex)
        elif hcindex>=index_starting[1] and hcindex<=index_ending[1]:
            x,y = hcindex2xy_ad(quart_block,hcindex - ncells_block)
            cor_origine=starting_point[1]
            x += cor_origine[0]
            y += cor_origine[1]
        elif hcindex>=index_starting[2] and hcindex<=index_ending[2]:
            x,y = hcindex2xy_bc(quart_block,hcindex - 2*ncells_block)
            cor_origine=starting_point[2]
            x += cor_origine[0]
            y += cor_origine[1]
        elif hcindex>=index_starting[3] and hcindex<=index_ending[3]:
            x,y = hcindex2xy_dc(quart_block,hcindex - 3*ncells_block)
            cor_origine=starting_point[3]
            x += cor_origine[0]
            y += cor_origine[1]
        else:
             print 'The  hcindex(AC) exceeds the maximum:',index_ending[3]
             sys.exit('index(AC) error')

    else:
        cor_position  = positions[hcindex]
        x = cor_position[0]
        y = cor_position[1]

    return x,y
##############################################################################

#-----------------------------CA-----------------------------------------------
def hcindex2xy_ca(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ac(n,n**2-1-hcindex) # hilbert curve symmetry
# force the vertex C which loacts at (n-1,n-1) in operator hcindex2xy_ad to be (0,0)
    x =x-(n-1)
    y =y-(n-1)
    return x,y
############################################################################

#----------------------------DB--------------------------------------------
def hcindex2xy_db(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ac(n,hcindex) # hilbert curve symmetry
# force the vertex C which loacts at (n-1,n-1) in operator hcindex2xy_ad to be (0,0)
    x =-x
    return x,y
###########################################################################

#-----------------------------------BD-----------------------------------
def hcindex2xy_bd(n,hcindex):
    assert(hcindex <= n**2 - 1)
    x,y = hcindex2xy_ac(n,hcindex) # hilbert curve symmetry
# force the vertex C which loacts at (n-1,n-1) in operator hcindex2xy_ad to be (0,0)
    y =-y
    return x,y
#########################################################################
