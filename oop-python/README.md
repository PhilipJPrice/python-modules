# Object-Oriented Programming

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
from ..moduleName1.moduleName2 import ClassName()
```

### __init__.py Defines Directory as Package
