
# Classes and Objects

**Adapted from materials by Tommy Guy and Anthony Scopatz**

## Object Orientation

**Object oriented programming** is a way of thinking about and defining how
different pieces of software and ideas work together. In objected oriented
programming, there are two main interfaces: **classes** and **objects**.

* **Classes** are types of things such as int, float, person, or square.
* **Objects** are **instances** of those types such a 1, 42.0, me, and a square
with side length 2.


Unlike functional or procedural paradigms, there are three main features that
classes provide.

* **Encapsulation:** Classes are containers that may have any kind of other
programming element living in them: variables, functions, and even other
classes. In Python, members of a class are known as **attributes** for normal
variables and **methods** for functions.


* **Inheritence:** A class may automatically gain all of the attributes and
methods from another class it is related to.  The new class is called a
**subclass** or sometimes a **subtype**.  Multiple levels of inheritance set up
a **class heirarchy**. For example:

    - `Shape` is a class with an `area` attribute.
    - `Rectangle` is a subclass of `Shape`.
    - `Square` is a subclass of `Rectangle` (which also makes it a subclass of
`Shape`).


* **Polymorphism:** Subclasses may override methods and attributes of their
parents in a way that is suitable to them.  For example:.

    - `Shape` is a class with an `area` method.
    - `Square` is a subclass of `Shape` that computes area by $x^2$.
    - `Circle` is a subclass of `Shape` that computes area by $\pi r^2$


If this seems more complicated than writing functions and calling them in
sequence that is because it is! However, obeject orientation enables authors to
cleanly separate out ideas into independent classes and potentially produce more
efficient code overall. It is also good to know because in many languages -
Python included - it is the way that you modify the type system.

## Basic Classes

Object oriented programming revolves around the creation and
manipulation of objects that have attributes and can do things. They can
be as simple as a coordinate with x and y values or as complicated as a
dynamic webpage framework. Here is the code for making a very simple class
that sets an attribute.

In[1]:

```
class MyClass(object):
    def me(self, name):
        self.name = name
```

In[2]:

```
my_object = MyClass()
```

In the object oriented terminology above:

- `MyClass` - a user defined type.
- `my_object` - a `MyClass` instance.
- `me()` - a `MyClass` method (member function)
- `self` - a reference to the object that is used to define method.  This must
be the first agument of any method.
- `name` - an attribute (member variable) of `MyClass`.
- `object` - a special class that should be the parent of all classes.

You *write* a class and you *create* and object.

We can check the type of the object we've created.

In[3]:

```
type(my_object)
```




    __main__.MyClass



We can directly set and access the name attribute.

In[4]:

```
my_object.name = 'Rachel'
print my_object.name
```


    Rachel


We can call the function to set the name attribute.

In[5]:

```
my_object.me('Azalee')
print my_object.name
```


    Azalee


**Hands on Example**

Write an Atom class with mass and velocity attributes and an energy() method.

In[8]:

```
# Atom class with mass and velocity attributes and an energy method

class Atom(object):
    
    # Setup function takes mass in amu and velocity in m/s
    def set_properties(self, m, v):
        self.mass = m * 1.66053892e-27 # convert mass from amu to kg
        self.velocity = v
        
    # Function to calculation kinetic energy
    def calc_energy(self):
        
        self.energy = 0.5 * self.mass * self.velocity**2

```

Let's try it out!

In[10]:

```
atom = Atom()
print "atom is of type", type(atom)

# Set and check properties of atom
atom.set_properties(12, 2e7)
print "\nMass in kg", atom.mass
print "\nVelocity in m/s", atom.velocity
atom.calc_energy()
print "\nEnergy in Joules", atom.energy

# Reset and check properties of atom
atom.set_properties(15, 2e27)
print "\n\n\nMass in kg", atom.mass
print "\nVelocity in m/s", atom.velocity
atom.calc_energy()
print "\nEnergy in Joules", atom.energy

# Get a new Atom and compare 
beta = Atom()
beta.set_properties(235, 1e6)
print atom.mass
print beta.mass
print atom.velocity
print beta.velocity
```


    atom is of type <class '__main__.Atom'>
    
    Mass in kg 1.992646704e-26
    
    Velocity in m/s 20000000.0
    
    Energy in Joules 3.985293408e-12
    
    
    
    Mass in kg 2.49080838e-26
    
    Velocity in m/s 2e+27
    
    Energy in Joules 4.98161676e+28
    2.49080838e-26
    3.902266462e-25
    2e+27
    1000000.0


In[23]:

```
class Parallelpipied(object):
    
    def __init__(self, h, w, l):
    
        self.height = h
        self.width = w
        self.length = l
        
    def calc_area(self):
        
        self.area = self.height * self.width
        
    def calc_volume(self):
        
        self.volume = self.height * self.width * self.length
```

In[24]:

```
my_shape = Parallelpipied(1.0, 2.0 ,3.0)
my_shape.calc_area()
print my_shape.area

my_shape.calc_volume()
print my_shape.volume
```


    2.0
    6.0


## Programatic Attribute Access

Python provides three built-in functions, `getattr()`, `setattr()`, and
`delattr()` to programticaly access an object's members.  These all take the
object and the string name of the attribute to be accessed.  This is instead of
using dot-access.

In[11]:

```
class A(object):
    a = 1
```

In[12]:

```
avar = A()
getattr(avar, 'a')
```




    1



In[13]:

```
setattr(avar, 'q', 'mon')
print avar.q
```


    mon


##Constructors

Usually you want to create an object with a set of initial or default values for
things. Perhaps an object needs certain information to be created. For
this you write a **constructor**. In python, constructors are just methods
with the special name ``__init__()``:

In[14]:

```
class Person(object):
    def __init__(self):
        self.name = "Rachel"
```

In[15]:

```
person = Person()
print person.name
```


    Rachel


Constructors may take arguements just like any other method or function.

In[16]:

```
class Person(object):
    def __init__(self, name, title="The Best"):
        self.name = name
        self.title = title
```

In[17]:

```
rachel = Person("Rachel")
print rachel.name, rachel.title
```


    Rachel The Best


In[18]:

```
azalee = Person("Azalee", "The Greatest")
print azalee.name, azalee.title
```


    Azalee The Greatest


Here is a more complex and realisitic example of a matrix class:

In[19]:

```
# Matrix defines a real, 2-d matrix.

class Matrix(object):
    # I am a matrix of real numbers

    def __init__(self, h, w):
        self._nrows = h
        self._ncols = w
        self._data = [0] * (self._nrows * self._ncols)

    def __str__(self):
        return "Matrix: " + str(self._nrows) + " by " + str(self._ncols)

    # reinitialize to zeros
    def reinit(self):
        self._data = [0] * (self._nrows * self._ncols)
    
    def setnrows(self, w):
        self._nrows = w
        self.reinit()

    def getnrows(self):
        return self._nrows

    def getncols(self):
        return self._ncols

    def setncols(self, h):
        self._ncols = h
        self.reinit()

    def setvalue(self, i, j, value):
        if i < self._nrows and j < self._ncols:
            self._data[i * self._nrows + j] = value
        else:
            raise Exception("Out of range")

    def multiply(self, other):
        # Perform matrix multiplication and return a new matrix.
        # The new matrix is on the left.
        result = Matrix(self._nrows, other.getncols())
        # Do multiplication...
        return result

    def inv(self):
        # Invert matrix 
        if self._ncols != self._nrows:
            raise Exception("Only square matrices are invertible")
        inverted = Matrix(self._ncols, self._nrows)
        inverted.setncols(self._ncols)
        inverted.setnrows(self._ncols)
        return inverted
```

## Interface vs. Implementation

Users shouldn't have to know *how* your program works in order to use
it.

The interface is a **contract** saying what a class knows how to do. The
code above defines matrix multiplication, which means that
`mat1.multiply(mat2)` should always return the right answer. It turns out
there are many ways to multiply matrices, and there are whole PhDs
written on performing efficient matrix inversion. The implementation is
the way in which the contract is carried out.

## Subclassing

If you want a to create a class that behaves mostly like another class,
you should not have to copy code. What you do is **subclass** and change the
things that need changing. When we created classes we were already
subclassing the built in python class "object."

For example, let's say you want to write a sparse matrix class, which
means that you don't explicitly store zero elements. You can create a
subclass of the Matrix class that redefines the matrix operations.

In[20]:

```
class SparseMatrix(Matrix):
    # I am a matrix of real numbers

    def __str__(self):
        return "SparseMatrix: " + str(self._nrows) + " by " + str(self._ncols)

    def reinit(self):
        self._data = {}

    def setValue(self, i, j, value):
        self._data[(i,j)] = value

    def multiply(self, other):
        # Perform matrix multiplication and return a new matrix.
        # The new matrix is on the left.
        result = SparseMatrix(self._nrows, other.getncols())
        # Do multiplication...
        return result

    def inv(self):
        # Invert matrix
        if self._nrows != self._rcols: 
            raise Exception("Only square matrices are invertible")
        inverted = SparseMatrix(self._ncols, self._nrows)

```

The SparseMatrix object is a Matrix but some methods are defined in the
*superclass* Matrix.  You can see this by looking at the dir of the SparseMatrix
and noting that it gets attributes from Matrix.

In[21]:

```
dir(SparseMatrix) 
```




    ['__class__',
     '__delattr__',
     '__dict__',
     '__doc__',
     '__format__',
     '__getattribute__',
     '__hash__',
     '__init__',
     '__module__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__weakref__',
     'getncols',
     'getnrows',
     'inv',
     'multiply',
     'reinit',
     'setValue',
     'setncols',
     'setnrows',
     'setvalue']



A more minimal and more abstact version of inheritence may be seen here:

In[22]:

```
class A(object):
    a = 1

class B(A):
    b = 2
    
class C(B):
    b = 42
    c = 3

x = C()
print x.a, x.b, x.c
```


    1 42 3


In[22]:

```

```

In[ ]:

```

```
