import numpy as np 

def function(x):

	r0 = x
	a2 = 4
	x = 3
	paths = []
	try:
		if r0 > 9:
			x = x/x
			paths.append(1)
		else:
			a2 = 2*r0
			a2 = a2-2
			x = 4*a2
			paths.append(2)
		if a2 > 3:
			r0 = r0/x
			a2 = a2*8
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a2 = x**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))