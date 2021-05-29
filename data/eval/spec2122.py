import numpy as np 

def function(x):

	a6 = 2
	n5 = x
	paths = []
	try:
		if n5 <= 5:
			n5 = n5*6
			n5 = x*8
			paths.append(1)
		else:
			a6 = a6*2
			a6 = 9/n5
			n5 = n5/7
			paths.append(2)
		if x <= 1:
			x = x+9
			paths.append(3)
		else:
			x = x-n5
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