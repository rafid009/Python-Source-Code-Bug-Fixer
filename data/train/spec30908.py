import numpy as np 

def function(x):

	a3 = 9
	v1 = x
	paths = []
	try:
		if v1 > 4:
			a3 = 9*3
			x = 2+4
			paths.append(1)
		else:
			a3 = a3*6
			v1 = v1+1
			paths.append(2)
		if v1 > 5:
			v1 = v1*2
			x = x-4
			a3 = 4/5
			paths.append(3)
		else:
			x = 2-x
			v1 = 1*x
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))