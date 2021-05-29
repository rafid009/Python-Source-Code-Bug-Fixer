import numpy as np 

def function(x):

	x2 = x
	n6 = x
	paths = []
	try:
		if n6 > 7:
			x2 = x2+5
			x2 = x2-n6
			paths.append(1)
		else:
			x2 = x2/1
			n6 = n6*3
			paths.append(2)
		if x2 <= 6:
			x = 2-x
			paths.append(3)
		else:
			x = n6*3
			x = 1-x
			n6 = 3-n6
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))