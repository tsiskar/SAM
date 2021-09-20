#!/usr/bin/env python
# coding: utf-8

# AMUSE tutorial on particle sets
# ====================
# 
# 
# AMUSE particle sets are a handy tool for storing data

# In[11]:


#Load in the amuse units module
from amuse.units import units
#from amuse.lab import Particles1
from amuse.lab import Particles, units


# In[12]:


# Declare a single particle
sun_and_earth = Particles(2)
sun = sun_and_earth[0]
sun.mass = 1 | units.MSun
sun.position = (0,0,0) | units.au
sun.velocity = (0,0,0) | units.kms
print("Sun=", sun)


# In[13]:


# Now declare the Earth
import random
from amuse.units.constants import G
earth = sun_and_earth[1]
earth.mass = 1 | units.MEarth
earth.position = (1, 0, 0) | units.au
true_anomaly=random.randint(1,90) | units.rad
def relative_orbital_velocity(mass, distance):
    return (G*mass/distance).sqrt()
vorb = relative_orbital_velocity(sun_and_earth.mass.sum(), 
                                earth.position.sum())
earth.velocity = (0, 1, 0) * vorb
print("Earth=", earth)


# In[14]:


sun_and_earth.move_to_center()
print(sun_and_earth)


# Now, let's give the particles a specific name (or other attribute)

# In[15]:


setattr(sun_and_earth, "name", "")
sun_and_earth.name = ["sun", "earth"]


# How we have declared the particles and moved them to the center of mass. We can also search for a specific particle. For example, the one with the "sun" in the attribute "name".

# In[16]:


earth = sun_and_earth[sun_and_earth.name=="earth"]
print("Sun=", sun)

We can add a moon in orbit around the earth
# In[17]:


moon = Particles(1)
moon.name = "moon"
moon.mass = 7.34767309e+22 | units.kg
moon.position = (384400, 0, 0) | units.km
true_anomaly=random.randint(1,90) | units.rad
vorb = relative_orbital_velocity(earth.mass + moon.mass, 
                                 moon.position.sum())
moon.velocity = (0, 1, 0) * vorb
print("moon=", moon)


# The moon, however, is not somewhere inside the Sun with zero velocity which is not good. We will have to replace the moon to make it orbit around the Earth. We do that by simply adding the positions and velocity of Earth to the moon's.

# In[18]:


moon.position += earth.position
moon.velocity += earth.velocity


# And we can add the moon to the Sun and Earth system

# In[19]:


sun_and_earth.add_particle(moon)


# Note the use of the singular here, because we only add a single particle to the particle set sun_and_earth.
# It is probably better to rename the sun_and_earth now.

# In[20]:


solarsystem = sun_and_earth


# It is important now to recenter the entire system, because by adding the moon we shifted the center of mass.

# In[21]:


solarsystem.move_to_center()
print("Solar system:", solarsystem)


# We can now manipulate the planetary system, or query it.
# for example by querying the masses.

# In[22]:


print("mass=", solarsystem.mass.in_(units.MEarth))


# This gives us a list of the masses of all objects, in units the the earth's mass. In fact, each of the particle's attributes is a simple numpy array: it can be assigned and manipulated as such.
# 
# Another way to ecquire the same information could be done as follows:

# In[23]:


print("mass=", solarsystem.mass/solarsystem[1].mass)


# In some (hopefully rare) cases you may want to use the particle set or its attributes as simple numpy arrays, without the units.
# This is easily achieved by stripping the unit from the array. This can be realied by explicitely querying the selected parameter with that specific unit.

# In[24]:


solarsystem.position.value_in(units.parsec)


# which, in this case, gives you a 2-dimensional *numpy.array* of the positions of star, planet and moon in units of a parsec.

# Now, you may want to query the particle set solarsystem.
# for example by asking what are all its attributes.
# this can be done as follows:

# In[25]:


dir(solarsystem)


# Or get some general help on the underlying particle class

# In[26]:


help(solarsystem)


# You have performed some rudimentary operations on a particle set.
# It is now time to experiment a little for yourself.
# 
# 
# Assignmnets and questions:
# ---------------
# 
# ### Assignment 1:
# Add the planet Jupiter (see [Wikipedia](https://en.wikipedia.org/wiki/Jupiter)) to your small planetary system.
# 
# ### Assignment 2:
# Your planetary system is notoriously planar, and initialy the earth and moon are positioned along the Cartesian x-axis with the velocity vector in the Cartesian y-direction. 
# 
# Make the Sun-Earth-Moon system more realistic by introducing a small inclination to the Earth's and Moon's orbits and by giving them a random mean anomaly.
# 
# The [Orbital element module](https://github.com/amusecode/amuse/blob/main/src/amuse/ext/orbital_elements.py) of AMUSE could come in handy. 
# 
# ### Assignment 3:
# Calculate the total  gravitational binding energy of solarsystem.
# 
# Now displace the entire particle set by 100 parsec and give it a linear velocity of 100km/s in the z-direction.
# Then calculate the binding energy of the system again.
# 
# Did the binding energy of the Solar system change by this translation?
# 
# ### Question 1:
# Particle sets have the attribute *get_binaries()*.
# If you use this function to check the binaries in your system you will find that (without Jupiter) you have 3 binaries. Explain why the Sun is in a binary with the Moon. You may want to take a look at the [source code](https://github.com/amusecode/amuse/blob/main/src/amuse/datamodel/particle_attributes.py).
# 
# ### Assignment 4:
# Generate another particle set with a 2 solar-mass star and two planets of 10 and 100 Earth masses in cirular orbits at 0.1 and 0.6 au. Place this second planetary system at apocenter around your Solar system (true anomaly of 180 degrees) at a semimajor axis of 60 au with an eccentricity of 0.6.
# Then move the entire system to the center of mass.
# 
# ### Question 2:
# Which of the orbits of the binary star with planets from *Assignment 4* has the highest binding energy?

# In[27]:


#Assignment 1
Jupiter = Particles(1)
Jupiter.name = "Jupiter"
Jupiter.mass =1.8982e+27 | units.kg
Jupiter.position = (5.2, 0, 0) | units.AU
vorb = relative_orbital_velocity(sun.mass + Jupiter.mass, 
                                 Jupiter.position.sum())
Jupiter.velocity = (0, 1, 0) * vorb
print("Jupiter=", Jupiter)


# In[28]:


#Assignment 2 done, true_anomaly added


# In[51]:


#Assignment3
rse=149597871 | units.km
rme=384400 | units.km
rms=149597871 | units.km
BE=-G*earth.mass*sun.mass/(rse)-G*earth.mass*moon.mass/rme-G*moon.mass*sun.mass/rms
print("Binding energy of sun-earth-moon system is", BE)


# In[ ]:





# In[ ]:





# In[ ]:




