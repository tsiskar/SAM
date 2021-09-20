#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Load in the amuse units module
from amuse.units import units


# In[19]:


# Declare some variables
mstar = 1 | units.MSun
rstar = 1 | units.RSun


# In[20]:


# calculate surface escape speed
# this requires the gravitational constant to be declared
G = 6.67e-11 | units.m**3 * units.kg**-1 * units.s**-2
vesc = (2*G*mstar/rstar).sqrt()


# In[21]:


print("The escape speed is:", vesc)


# In[22]:


print("The escape speed is:", vesc.in_(units.kms))


# In[7]:


from amuse.units.constants import G
vesc = (2*G*mstar/rstar).sqrt()
print("The escape speed is:", vesc.in_(units.kms))


# In[8]:


#Assignment 1
#Calculate the orbital velocity of the planet Earth in orbit around the Sun

vorb=(G*mstar/rstar).sqrt()
print("The orbital velocity is:", vorb.in_(units.kms))


# In[9]:


from amuse.units.constants import G
vorb=(G*mstar/rstar).sqrt()
print("The orbital velocity is:", vorb)


# In[26]:


#Assignment 2
#Calculate the escape speed of the supermassive black hole in the Galactic center from 
#the pericenter of S2 (the star famously used to characterize the central supermassive black hole).
mS2=14 | units.MSun
rS2=120| units.AU
vescBH = (2*G*mS2/rS2).sqrt()
print("The escape speed is:", vescBH.in_(units.kms))
print (vescBH)


# In[11]:


#question 1 ?


# In[12]:


#Question 2
#Sun's Luminosity
from amuse.units.constants import Stefan_hyphen_Boltzmann_constant
from amuse.units.constants import pi
eft=5772
L1=4*pi*(rstar**2)*Stefan_hyphen_Boltzmann_constant*(eft**4)
L2=1 | units.LSun

print("The Luminosity via Wikipedia is:", L1)
print("The Luminosity via AMUSE is:", L2)


# In[ ]:





# In[ ]:




