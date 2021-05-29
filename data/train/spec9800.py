import numpy as np 

def function(x):

	e0 = 3
	s2 = 7
	paths = []
	try:
		if s2 >= 7:
			e0 = 7/x
			paths.append(1)
		else:
			e0 = e0/1
			x = 2-9
			x = 5+5
			paths.append(2)
		if x > 8:
			s2 = 0*0
			paths.append(3)
		else:
			s2 = e0-e0
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))