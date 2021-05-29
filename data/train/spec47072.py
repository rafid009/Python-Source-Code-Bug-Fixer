import numpy as np 

def function(x):

	e2 = 3
	f9 = 9
	paths = []
	try:
		if e2 <= 2:
			e2 = e2*0
			f9 = 8+9
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if e2 < 7:
			x = 9-x
			f9 = f9-f9
			paths.append(3)
		else:
			f9 = f9*8
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))