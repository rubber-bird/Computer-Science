

def twoSum(lll, target):
	result = []
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if(list[i] + list[j] == target):
            	res.append(i)
                res.append(j)
                return res

def main():
	a = [2,7,11,15]
	l = 9
	print(twoSum(a,l))

if __name__ == '__main__':
	main()