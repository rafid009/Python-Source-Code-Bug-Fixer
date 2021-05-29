import numpy as np 

def function(x):

	n7 = 6
	j8 = 3
	paths = []
	try:
		if x < 1:
			n7 = n7/x
			j8 = 9/n7
			j8 = 5*j8
			paths.append(1)
		else:
			j8 = 1*9
			j8 = 5+n7
			paths.append(2)
		if x >= 9:
			n7 = n7*1
			paths.append(3)
		else:
			x = 6+n7
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