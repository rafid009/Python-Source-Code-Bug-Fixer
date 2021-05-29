import numpy as np 

def function(x):

	r2 = x
	a4 = 7
	x = 5
	paths = []
	try:
		if r2 > 0:
			r2 = 2/r2
			r2 = r2*a4
			r2 = r2-2
			paths.append(1)
		else:
			a4 = 4*a4
			a4 = a4+9
			paths.append(2)
		if a4 < 2:
			r2 = a4/r2
			x = 0+2
			x = x*3
			paths.append(3)
		else:
			a4 = a4*r2
			a4 = a4-1
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		a4 = a4**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))