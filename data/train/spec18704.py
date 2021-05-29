import numpy as np 

def function(x):

	e1 = x
	a8 = 1
	paths = []
	try:
		if a8 <= 0:
			e1 = x/a8
			a8 = a8*x
			e1 = e1*e1
			paths.append(1)
		else:
			e1 = x/4
			a8 = 8-a8
			paths.append(2)
		if a8 < 7:
			x = 8*x
			paths.append(3)
		else:
			a8 = a8/2
			a8 = a8*0
			a8 = x-a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))