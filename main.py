import os

def permission_tekshirish(fayl_nomi):
    try:
        return os.access(fayl_nomi, os.R_OK)
    except Exception as e:
        return False

fayl_nomi = input("Fayl nomini kiriting: ")
print(permission_tekshirish(fayl_nomi))
```

```python
import os

def permission_tekshirish(fayl_nomi):
    try:
        return os.access(fayl_nomi, os.W_OK)
    except Exception as e:
        return False

fayl_nomi = input("Fayl nomini kiriting: ")
print(permission_tekshirish(fayl_nomi))
```

```python
import os

def permission_tekshirish(fayl_nomi):
    try:
        return os.access(fayl_nomi, os.X_OK)
    except Exception as e:
        return False

fayl_nomi = input("Fayl nomini kiriting: ")
print(permission_tekshirish(fayl_nomi))
```

```python
import os

def permission_tekshirish(fayl_nomi):
    try:
        return os.access(fayl_nomi, os.R_OK | os.W_OK | os.X_OK)
    except Exception as e:
        return False

fayl_nomi = input("Fayl nomini kiriting: ")
print(permission_tekshirish(fayl_nomi))
