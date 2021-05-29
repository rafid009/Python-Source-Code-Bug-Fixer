import numpy as np 

def function(x):

	f2 = x
	a1 = 3
	paths = []
	try:
		if x > 8:
			x = 4*x
			f2 = f2/x
			paths.append(1)
		else:
			f2 = a1/f2
			a1 = a1/8
			paths.append(2)
		if f2 > 0:
			f2 = x-x
			paths.append(3)
		else:
			f2 = f2*0
			a1 = f2/a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))