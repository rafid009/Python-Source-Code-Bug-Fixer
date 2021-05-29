import numpy as np 

def function(x):

	e0 = x
	a0 = x
	paths = []
	try:
		if a0 > 4:
			x = x-x
			a0 = 5/a0
			e0 = 1-8
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if x <= 0:
			x = 7+x
			e0 = 5+a0
			a0 = x*7
			paths.append(3)
		else:
			e0 = e0*0
			e0 = 7-e0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		e0 = a0**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))