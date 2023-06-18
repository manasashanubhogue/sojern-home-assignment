###  Utility function to compare versions

Compare two version numbers version1 and version2.
If version1 > version2 return 1
If version1 < version2 return -1
otherwise return 0

#### Setup & Execution
``` 
cd compare-versions
python version_utility.py 'version1' 'version2'
```

#### Testing

``` python -m unittest test_utility.py ```

### Example

```
python version_utility.py '2.2.5.2' '2.2.5.0.0.0' 
1

python version_utility.py '2.2.5' '2.2.5' 
0

python version_utility.py '2.2.5' '2.2.5.1' 
-1
```
