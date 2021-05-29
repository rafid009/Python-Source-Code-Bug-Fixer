import numpy as np 

def function(x):

	v3 = x
	n9 = x
	paths = []
	try:
		if n9 < 7:
			n9 = n9/4
			paths.append(1)
		else:
			n9 = v3/n9
			x = 4/x
			paths.append(2)
		if x >= 4:
			x = n9*0
			x = v3*v3
			paths.append(3)
		else:
			x = 9*x
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