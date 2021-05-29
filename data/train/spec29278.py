import numpy as np 

def function(x):

	p8 = 7
	k7 = 3
	paths = []
	try:
		if p8 >= 6:
			x = x-7
			paths.append(1)
		else:
			p8 = p8+9
			paths.append(2)
		if p8 > 6:
			p8 = 1-4
			k7 = 2/6
			k7 = k7-6
			paths.append(3)
		else:
			x = 4*6
			p8 = 9/p8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))