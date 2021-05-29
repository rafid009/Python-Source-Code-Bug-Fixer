import numpy as np 

def function(x):

	a9 = 1
	i5 = x
	paths = []
	try:
		if x < 2:
			i5 = a9*x
			i5 = i5-8
			paths.append(1)
		else:
			a9 = x-x
			i5 = i5-4
			paths.append(2)
		if x > 8:
			i5 = i5/6
			i5 = 5*i5
			paths.append(3)
		else:
			a9 = i5-a9
			x = a9/1
			a9 = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))