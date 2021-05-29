import numpy as np 

def function(x):

	h7 = 2
	e3 = x
	x = 4
	paths = []
	try:
		if h7 < 7:
			e3 = 7*e3
			paths.append(1)
		else:
			h7 = 0-4
			h7 = 2*h7
			e3 = e3-6
			paths.append(2)
		if e3 >= 5:
			e3 = e3*x
			e3 = h7+3
			paths.append(3)
		else:
			h7 = h7*9
			x = e3/5
			h7 = h7+2
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		e3 = e3**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))