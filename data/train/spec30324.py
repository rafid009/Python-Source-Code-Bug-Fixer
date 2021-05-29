import numpy as np 

def function(x):

	r6 = 2
	n6 = x
	paths = []
	try:
		if x <= 3:
			n6 = 3/x
			x = x+8
			paths.append(1)
		else:
			n6 = 1-n6
			paths.append(2)
		if x >= 3:
			x = r6*9
			r6 = r6-3
			n6 = n6/5
			paths.append(3)
		else:
			n6 = 3+6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		n6 = r6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))