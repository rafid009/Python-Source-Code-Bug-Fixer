import numpy as np 

def function(x):

	a0 = x
	e6 = x
	paths = []
	try:
		if x > 4:
			e6 = e6/6
			a0 = a0*2
			paths.append(1)
		else:
			a0 = 2+a0
			e6 = e6-8
			x = 1*x
			paths.append(2)
		if x < 9:
			x = e6-x
			e6 = e6/1
			paths.append(3)
		else:
			e6 = e6+e6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))