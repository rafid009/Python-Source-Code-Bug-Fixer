import numpy as np 

def function(x):

	f0 = 6
	n3 = 2
	paths = []
	try:
		if n3 <= 1:
			n3 = n3/6
			n3 = n3*x
			paths.append(1)
		else:
			f0 = 4+2
			n3 = 9+n3
			paths.append(2)
		if n3 >= 4:
			n3 = n3+9
			paths.append(3)
		else:
			n3 = n3-9
			f0 = 7+f0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))