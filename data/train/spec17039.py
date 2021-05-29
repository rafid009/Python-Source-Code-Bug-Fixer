import numpy as np 

def function(x):

	v5 = x
	n6 = 8
	paths = []
	try:
		if v5 >= 9:
			n6 = 7+n6
			paths.append(1)
		else:
			v5 = 3/v5
			x = n6*7
			n6 = 3*n6
			paths.append(2)
		if x < 6:
			n6 = 2+v5
			paths.append(3)
		else:
			n6 = n6-n6
			x = x-3
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))