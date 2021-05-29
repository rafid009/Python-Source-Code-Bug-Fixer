import numpy as np 

def function(x):

	n6 = x
	r6 = x
	paths = []
	try:
		if r6 >= 2:
			n6 = n6+5
			paths.append(1)
		else:
			x = n6/x
			x = r6-2
			n6 = x+5
			paths.append(2)
		if n6 > 5:
			n6 = n6-n6
			x = 6*n6
			paths.append(3)
		else:
			x = x-9
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