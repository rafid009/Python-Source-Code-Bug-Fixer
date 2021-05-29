import numpy as np 

def function(x):

	n4 = 8
	x7 = 8
	paths = []
	try:
		if n4 >= 7:
			x = n4*x
			x = x+3
			x7 = x+x7
			paths.append(1)
		else:
			n4 = n4*x
			n4 = 4+n4
			paths.append(2)
		if n4 <= 8:
			n4 = 2+n4
			x7 = x7*9
			n4 = 5-8
			paths.append(3)
		else:
			x = 1*x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))