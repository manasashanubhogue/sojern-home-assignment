import sys

def compare_versions(version1, version2):
    # assuming the versions are strings and non-empty
    v1_list = version1.split('.')
    v2_list = version2.split('.')
    len_v1_list = len(v1_list)
    len_v2_list = len(v2_list)

    # Compare each part of the version numbers
    for i in range(max(len_v1_list, len_v2_list)):

        v1 = int(v1_list[i]) if i<len_v1_list else 0
        v2 = int(v2_list[i]) if i<len_v2_list else 0

        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

    return 0

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python version_utility.py \'version1\' \'version2\'')
        sys.exit(1)

    version1 = sys.argv[1]
    version2 = sys.argv[2]

    result = compare_versions(version1, version2)
    print(result)