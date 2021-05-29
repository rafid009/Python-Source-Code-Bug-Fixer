import numpy as np 

def function(x):

	f6 = x
	n1 = x
	paths = []
	try:
		if x <= 3:
			x = x-1
			x = 5/x
			n1 = n1+n1
			paths.append(1)
		else:
			x = 2*x
			n1 = 8/n1
			f6 = f6/5
			paths.append(2)
		if x > 5:
			f6 = 1*f6
			x = 2-2
			paths.append(3)
		else:
			n1 = n1+7
			n1 = 8-f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))