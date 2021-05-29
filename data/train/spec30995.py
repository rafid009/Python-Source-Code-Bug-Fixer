import numpy as np 

def function(x):

	i9 = 6
	n6 = 9
	paths = []
	try:
		if n6 > 6:
			x = 4*x
			n6 = x/i9
			i9 = i9/6
			paths.append(1)
		else:
			x = i9-x
			paths.append(2)
		if i9 < 2:
			i9 = 4+i9
			n6 = n6*8
			n6 = n6*6
			paths.append(3)
		else:
			x = x-1
			i9 = 5-i9
			x = 4-i9
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))