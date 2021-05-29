import numpy as np 

def function(x):

	k6 = 2
	i7 = 9
	paths = []
	try:
		if i7 < 6:
			i7 = i7/7
			x = x-0
			i7 = k6*i7
			paths.append(1)
		else:
			k6 = x+i7
			i7 = 4-k6
			paths.append(2)
		if k6 > 5:
			i7 = x/1
			x = x-3
			k6 = k6-k6
			paths.append(3)
		else:
			x = 4*5
			i7 = x-k6
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))