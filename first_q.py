import sys

def sum_list(nums):
    total = sum(nums)
    return [total - d for d in nums]

def main():
    nums = [int(i) for i in sys.argv[1].split(',')]
    ans = sum_list(nums)
    print(ans)

if __name__ == '__main__':
    main()