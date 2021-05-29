import numpy as np 

def function(x):

	f2 = x
	x7 = 2
	x = 7
	paths = []
	try:
		if f2 >= 1:
			x7 = x7*1
			paths.append(1)
		else:
			x = 2*x
			x = x+x7
			x = x/x
			paths.append(2)
		if x > 8:
			x = x/x
			x = x7*x
			paths.append(3)
		else:
			x = f2/x7
			x7 = x7+2
			x7 = 2/3
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