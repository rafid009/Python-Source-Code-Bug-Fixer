import numpy as np 

def function(x):

	a8 = x
	n7 = x
	paths = []
	try:
		if n7 >= 9:
			n7 = n7+1
			n7 = n7+7
			paths.append(1)
		else:
			n7 = n7/9
			paths.append(2)
		if x <= 9:
			x = x-3
			x = x*9
			paths.append(3)
		else:
			a8 = a8/9
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		a8 = n7**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))