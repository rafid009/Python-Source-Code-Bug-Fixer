import numpy as np 

def function(x):

	a3 = 5
	i1 = x
	paths = []
	try:
		if i1 >= 7:
			i1 = 9*i1
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if x >= 8:
			a3 = 2+a3
			a3 = 5+a3
			paths.append(3)
		else:
			a3 = a3*x
			i1 = a3-4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		a3 = i1**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))