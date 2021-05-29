import numpy as np 

def function(x):

	n6 = x
	i4 = x
	paths = []
	try:
		if x < 7:
			x = 8+x
			paths.append(1)
		else:
			n6 = n6-x
			paths.append(2)
		if n6 <= 2:
			i4 = i4-0
			x = 3-x
			x = x*n6
			paths.append(3)
		else:
			n6 = n6+2
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))