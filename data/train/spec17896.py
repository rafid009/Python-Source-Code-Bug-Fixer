import numpy as np 

def function(x):

	f0 = 2
	e2 = x
	x = 5
	paths = []
	try:
		if f0 < 4:
			x = 5+x
			x = 2*5
			paths.append(1)
		else:
			e2 = x*3
			x = 4/x
			paths.append(2)
		if e2 > 3:
			e2 = f0*e2
			f0 = 8+f0
			x = 6/7
			paths.append(3)
		else:
			x = e2*f0
			f0 = 8*x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		e2 = e2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))