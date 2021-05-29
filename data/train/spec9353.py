import numpy as np 

def function(x):

	k6 = 5
	n9 = x
	x = x
	paths = []
	try:
		if n9 > 4:
			x = x*n9
			k6 = 5/2
			paths.append(1)
		else:
			x = x+6
			paths.append(2)
		if x >= 9:
			n9 = 1+0
			paths.append(3)
		else:
			x = x+k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))