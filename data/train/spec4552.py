import numpy as np 

def function(x):

	a6 = x
	t1 = 5
	paths = []
	try:
		if t1 >= 7:
			x = x+8
			a6 = a6/9
			x = a6-a6
			paths.append(1)
		else:
			a6 = 4/a6
			paths.append(2)
		if a6 >= 6:
			x = 1+t1
			a6 = a6-6
			x = x/8
			paths.append(3)
		else:
			a6 = a6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a6 = x**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))