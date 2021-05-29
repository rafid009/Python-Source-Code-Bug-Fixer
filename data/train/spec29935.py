import numpy as np 

def function(x):

	a6 = x
	e1 = x
	paths = []
	try:
		if a6 > 5:
			e1 = 8+e1
			paths.append(1)
		else:
			e1 = e1/4
			e1 = e1-7
			paths.append(2)
		if x > 1:
			e1 = e1/5
			paths.append(3)
		else:
			e1 = e1+6
			x = e1*e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))