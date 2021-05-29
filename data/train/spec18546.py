import numpy as np 

def function(x):

	n5 = 1
	q8 = 7
	paths = []
	try:
		if x > 8:
			x = x/x
			paths.append(1)
		else:
			x = 6+x
			n5 = 6-n5
			q8 = 1/8
			paths.append(2)
		if n5 > 9:
			x = 6-n5
			x = x+2
			paths.append(3)
		else:
			n5 = x*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))