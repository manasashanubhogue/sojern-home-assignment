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
![Screenshot 2023-06-18 at 16 23 00](https://github.com/manasashanubhogue/sojern-home-assignment/assets/6822599/011b7589-bfbe-432b-a014-6a99c1be37cb)
