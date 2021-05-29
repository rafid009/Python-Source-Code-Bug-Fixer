import numpy as np 

def function(x):

	t9 = x
	n8 = x
	paths = []
	try:
		if x < 6:
			x = x-1
			paths.append(1)
		else:
			x = x-x
			t9 = t9*7
			n8 = n8+8
			paths.append(2)
		if n8 < 8:
			n8 = n8*t9
			paths.append(3)
		else:
			n8 = n8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))