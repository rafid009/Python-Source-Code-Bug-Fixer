import numpy as np 

def function(x):

	n5 = x
	v7 = 2
	paths = []
	try:
		if x <= 9:
			n5 = 9*n5
			v7 = v7/1
			v7 = v7+n5
			paths.append(1)
		else:
			x = 2/1
			v7 = 1+v7
			paths.append(2)
		if v7 <= 0:
			x = 8-x
			v7 = v7/v7
			v7 = n5*v7
			paths.append(3)
		else:
			n5 = n5+7
			n5 = x/1
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