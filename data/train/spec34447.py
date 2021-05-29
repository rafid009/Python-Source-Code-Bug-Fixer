import numpy as np 

def function(x):

	r9 = 8
	n6 = 2
	paths = []
	try:
		if n6 <= 8:
			n6 = 9*1
			paths.append(1)
		else:
			n6 = n6*8
			n6 = n6+2
			paths.append(2)
		if r9 < 1:
			r9 = n6-4
			paths.append(3)
		else:
			r9 = r9/r9
			r9 = 8+r9
			x = x+x
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