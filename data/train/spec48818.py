import numpy as np 

def function(x):

	n4 = 0
	i9 = 0
	x = x
	paths = []
	try:
		if x > 5:
			x = n4-8
			n4 = n4/3
			i9 = i9+7
			paths.append(1)
		else:
			i9 = x-i9
			i9 = i9-0
			paths.append(2)
		if n4 < 6:
			i9 = 3*i9
			paths.append(3)
		else:
			x = x*i9
			i9 = 1/i9
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		n4 = i9**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))