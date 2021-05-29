import numpy as np 

def function(x):

	e6 = 3
	s7 = x
	paths = []
	try:
		if x <= 4:
			x = 5*e6
			x = 6+2
			x = x+s7
			paths.append(1)
		else:
			e6 = e6/7
			e6 = 6-6
			e6 = 2-5
			paths.append(2)
		if e6 <= 7:
			s7 = e6+s7
			x = 5*e6
			paths.append(3)
		else:
			s7 = 8*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))