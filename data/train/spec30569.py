import numpy as np 

def function(x):

	a1 = 2
	e4 = 4
	paths = []
	try:
		if a1 < 0:
			x = x+1
			paths.append(1)
		else:
			e4 = 1/a1
			e4 = e4/1
			a1 = a1/6
			paths.append(2)
		if x >= 1:
			a1 = e4-5
			a1 = x+a1
			a1 = a1+e4
			paths.append(3)
		else:
			a1 = a1/3
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))