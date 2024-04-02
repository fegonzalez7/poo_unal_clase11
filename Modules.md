# Modules (and packages)

A module in Python is actually... an object! It acts as something like the super() or self objects but of directory or file, compressed or not. It is most often a set of files and directories (although not always, since .zip files can also be imported and these do not have the usual file system organization) that contain blocks of code or more files, respectively.

> *A module is an **object** that acts as an organizational unit within another file.*
>
> That's why they have attributes like ``__path__`` or ``__name__``, which intend to facilitate the access to what they store via namespaces.

A file module contains definitions of functions and classes, and could even contain its own ``__main__``, just as an average ``.py`` file. On the other hand, a package module contains module files and/or subpackages. Furthermore, the only difference between file and package modules is the ``__path__`` attribute that the latter has: it specifies the paths to the modules and subpackages it may contain.

Before we continue, some clarifications need to be made before we go on:

- A ``.py`` file contains a script, which is a set of definitions and an active implementation of those that serves as an input to the interpreter, which will in turn execute it.
- Everything defined in Python has a name, whether it is a variable, a function or a class, a name within the namespace of the active script is given to every single one of them. The reason is because even the active script can serve as a base for a module. Therefore, it must have a collection of names to which another module could access when imports the script. All the names defined in a module can be accessed using the [``dir()``](https://docs.python.org/3/library/functions.html#dir) function.
- Any package module will have the attribute [``__path__``](https://docs.python.org/3/reference/import.html#package-path-rules), initialized with an iterable of strings that, when iterated over, create all the paths to other subpackage or file modules.

## Importing

Modules gain considerable relevance when aiming at modularity, simplicity and reusability of code, because when, in your current script you're in need of a function from another file, or need to create an object you had defined in a different project in a different directory, modules' importing is there to save the day.

It essentially consists in calling a function known as [``__import__()``](https://docs.python.org/3/library/functions.html#import__). This function searches for a module's ``__name__`` (one of its attributes) and, if it finds one or more modules with a matching name, it returns the modules and binds (fastens or secures) a name, stored in the ``__name__`` variable, to them.

This name will in turn become a namespace in the script you're currently working on while simultaneously acting as an object that is the actual module, which you can use to get access to all the definitions and be able to redefine them.

Now, you may ask, but if a module is an object, what class does it belong to? Well, my friend, we'll get a helping hand from our beloved C++:

> In C++, importing was done, before ``import`` was recently implemented, with the ``#include`` keyword. After using that keyword, you'll call a header file which will allow you to do what modules allow you to do in Python. Now, the key is in what are these header files: they are a *class definition* of a class that contains all the functions and variables you defined in another file. So, when you include the header file somewhere, you are actually creating an instance of the class declared in the headr file that can now be used in the current file. 
> 
> How does this help us understand where do modules come from? Well, modules are simply instances off the header files that are implicitely created when importing. So Python makes sure to create the modules' class so that we only have to call the singleton object of that class.

The whole mechanism in Python involves calling multiple functions to initialize and set correctly the module object whilst dealing with the paths of the modules' location. It can be found [here](https://docs.python.org/3/reference/import.html#), but in summary importing consists in finding, loading and creating an object module, identified with a namespace, that can be used in a file, so that all the method, classes and attributes that are part of the module can be called, accessed or redefined (Note: Python runs the code in the module file when the module is bound to a name, so prior to its use).

## Absolute imports
When it comes to the way modules are called in a file, there are two types of imports: absolute and relative. The first one explicitly states the location of a module within a root package, i.e., it states the path to access the module from the parent package module (the one that's not a subpackage of any package) to the subpackage the module file is in or the actual module. It is good practice to first use the ``from`` keyword to indicate the path to the module and then use ``import`` to state which functions or classes from the module need to be imported, but it can also be done solely with ``import`` if all of the module's content will be used.

```Python
from root.sub1.sub2.sub3.module import function1, class1

import root.subp1.subp2.subp3.module
from root.sub1.sub2.sub3.module import * #Also imports all of the module's content except for the ones that are defined with an underscore(_)
```

## Relative imports
These type of imports, as their name indicates, use a reference to call a module, and that reference is the active module's package or directory. To indicate where is the module to be imported relative to the current module dots are used: to the left they mean they are accessing the module from a parent, grandparent, or so on package from the current directory (one dot means the module right after it is in the same directory as the current module), whereas to the right it means they are accessing a child, grandchild, ... package relative to the current module's directory. Certainly, there must be words in between the dots so ``import`` knows which module from an upper or lower level the module to be imported is located. Let's look at the syntax using the following file system:

root/
│   mod_root.py
│
└── sub1/
    │   mod_sub1.py
    │
    └── sub2/
        │   mod.py
        |   same_level.py
        │ 
        └── sub3/
            │   mod_sub3.py
└── sub4/
    │   mod_sub4.py



```Python
from .sub3.mod_sub3 import function1 #Importing from a child 

from .sub1.mod_sub1 import function2 #Importing from a parent

from .sub4.mod_sub4. import class1 #Importing from a path adjacent to a parent
```

It is less straightforward than an absolute import, and could cause namespace troubles with same-name modules if there are regular packages. However, when making a package of modules, it is more recommended to implement it, since otherwise the paths could be unnecesarily long and too complex to process. In general though, an absolute import will be the best choice.

## Namespace and regular packages

Packages are a way of structuring a set of modules using *dotted module names*, which are pretty much the same as a path in a directory, just applied to modules and not files and changing the ``/`` for ``.``. The only difference with file modules is the attribute ``__path__`` and the fact that they are directories. However, there can be one more difference, the ``__init__.py`` file, whose implementation depends on the type of package you choose to use:

### Namespace packages

These are available since Python 3.3, and they are an update simmilar to the one the MRO (Method Resolution Order) had with its C3 linearization algorithm implementation: Python makes sure to sort out any same-name problems the regular packages have by binding any packages with the same name different namespaces. Since their path must be different (they are at a different level, i.e., at a different package, since there cannot be more than one package with the same name in the same directory by default), Python will make sure to interpret them differently when imported. Also, the interpreter will set the ``__path__`` attribute to any directories specified in an import name to treat them as package modules, avoiding the necessity of implementing an ``__init__.py``, which often doesn't contain anything (only modules' attributes can be redefined here, but that's not often done).

So they are a newer version of module packages that it is recommended to use.

### Regular packages

The classical Python packages are distinguished from the namespace ones because of the presence of an ``__init__.py`` file inside them. As mentioned previously, this file can be useful to configure specific settings of a module that will alter how the module ``sys`` imports the other ones. For compatibility with older versions, it is recommended.