import numpy as np 

def function(x):

	a4 = 4
	n1 = x
	paths = []
	try:
		if a4 < 7:
			a4 = a4-4
			paths.append(1)
		else:
			n1 = 2*7
			a4 = a4/a4
			paths.append(2)
		if n1 < 9:
			a4 = x*a4
			paths.append(3)
		else:
			a4 = 9+2
			n1 = n1/n1
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		a4 = n1**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))