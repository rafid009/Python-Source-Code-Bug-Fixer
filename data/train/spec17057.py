import numpy as np 

def function(x):

	v1 = x
	n6 = 0
	paths = []
	try:
		if n6 <= 9:
			v1 = 6/v1
			n6 = n6-0
			x = x-7
			paths.append(1)
		else:
			n6 = n6+3
			paths.append(2)
		if x >= 1:
			n6 = n6*5
			n6 = n6-6
			paths.append(3)
		else:
			v1 = v1+v1
			n6 = n6/3
			v1 = x*v1
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