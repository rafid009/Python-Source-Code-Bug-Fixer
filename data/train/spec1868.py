import numpy as np 

def function(x):

	p4 = 1
	v7 = 9
	paths = []
	try:
		if x > 9:
			v7 = 7*1
			v7 = v7-v7
			p4 = v7*5
			paths.append(1)
		else:
			x = 3-x
			v7 = v7-3
			paths.append(2)
		if x < 9:
			x = 9/v7
			v7 = x-v7
			paths.append(3)
		else:
			v7 = v7*v7
			v7 = 4-4
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))