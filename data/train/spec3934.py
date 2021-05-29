import numpy as np 

def function(x):

	v3 = x
	n6 = 9
	paths = []
	try:
		if x <= 2:
			v3 = v3/9
			n6 = 0+v3
			x = n6*1
			paths.append(1)
		else:
			x = n6-7
			x = 3/x
			paths.append(2)
		if x >= 9:
			v3 = 6+v3
			n6 = 7*n6
			x = n6-x
			paths.append(3)
		else:
			x = x*5
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