import numpy as np 

def function(x):

	e9 = 7
	a5 = x
	paths = []
	try:
		if e9 <= 4:
			a5 = 4+e9
			a5 = a5*x
			paths.append(1)
		else:
			a5 = 2/5
			e9 = e9*4
			paths.append(2)
		if e9 > 8:
			e9 = e9+e9
			x = x+x
			paths.append(3)
		else:
			x = 8*a5
			e9 = x*0
			a5 = 8+2
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