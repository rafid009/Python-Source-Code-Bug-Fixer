import numpy as np 

def function(x):

	n6 = x
	j9 = x
	paths = []
	try:
		if n6 > 7:
			n6 = 5+n6
			paths.append(1)
		else:
			j9 = 7-j9
			paths.append(2)
		if n6 < 9:
			x = x/5
			paths.append(3)
		else:
			j9 = j9+7
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))