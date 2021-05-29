import numpy as np 

def function(x):

	r3 = x
	n3 = x
	paths = []
	try:
		if x > 0:
			r3 = r3+1
			r3 = 2-x
			paths.append(1)
		else:
			r3 = r3*7
			n3 = 0-2
			x = 4+x
			paths.append(2)
		if x > 5:
			n3 = n3*4
			paths.append(3)
		else:
			n3 = n3-0
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