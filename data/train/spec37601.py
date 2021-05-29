import numpy as np 

def function(x):

	l1 = 5
	x3 = 5
	paths = []
	try:
		if l1 > 3:
			l1 = l1+4
			x = x+2
			x = x+7
			paths.append(1)
		else:
			x3 = l1*x3
			paths.append(2)
		if x3 >= 5:
			x3 = 5*l1
			x3 = 8-x3
			paths.append(3)
		else:
			x3 = 7-x3
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x3 = x3**0.5
		return x3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))