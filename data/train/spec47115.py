import numpy as np 

def function(x):

	k2 = 4
	n3 = 7
	paths = []
	try:
		if k2 >= 4:
			n3 = n3+6
			paths.append(1)
		else:
			k2 = k2*x
			paths.append(2)
		if n3 <= 8:
			k2 = 2*x
			n3 = n3-x
			paths.append(3)
		else:
			n3 = 2-n3
			x = x+k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))