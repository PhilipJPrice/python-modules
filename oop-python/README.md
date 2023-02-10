# Object-Oriented Programming

## Sources

[The Python Apprentice by Robert Smallshire, Austin Bingham](https://www.packtpub.com/product/the-python-apprentice/9781788293181)

[Python 3 Object-Oriented Programming - Third Edition by Dusty Phillips](https://www.packtpub.com/product/python-3-object-oriented-programming-third-edition/9781789615852)

[Python Object-Oriented Programming - Fourth Edition by Steven F. Lott, Dusty Phillips](https://packtpub.com/product/python-object-oriented-programming-fourth-edition/9781801077262)

## Classes

### To run code and then drop to the interactive interpreter

```
python -i file.py
```

### Absolute Imports

```
import fileName.moduleName
moduleVar = fileName.moduleName.ClassName()
```

```
from fileName.moduleName import ClassName
moduleVar = ClassName()
```

```
from fileName import moduleName
moduleVar = moduleName.ClassName()
```

### Relative Imports

```
from .moduleName import ClassName()
```

```
from ..moduleName import ClassName()
```

```
from ..packageName.moduleName import ClassName()
```

### __init__.py Defines Directory as Package
