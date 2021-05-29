import numpy as np 

def function(x):

	e2 = 5
	h2 = x
	x = x
	paths = []
	try:
		if x <= 5:
			h2 = h2-7
			paths.append(1)
		else:
			e2 = 5-2
			x = 0+x
			h2 = e2+h2
			paths.append(2)
		if x >= 0:
			h2 = x*e2
			paths.append(3)
		else:
			x = 4*x
			e2 = 8-e2
			e2 = e2+1
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		e2 = h2**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))