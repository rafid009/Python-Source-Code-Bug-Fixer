import numpy as np 

def function(x):

	a4 = 4
	v1 = 4
	paths = []
	try:
		if v1 > 3:
			v1 = v1/5
			a4 = a4+v1
			v1 = x+v1
			paths.append(1)
		else:
			a4 = 2*a4
			a4 = a4/5
			paths.append(2)
		if x > 1:
			x = 7/2
			a4 = x*a4
			x = 2-8
			paths.append(3)
		else:
			x = x+a4
			a4 = x+0
			v1 = 6+v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))