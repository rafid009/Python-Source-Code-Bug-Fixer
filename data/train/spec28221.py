import numpy as np 

def function(x):

	b5 = 2
	e3 = 2
	paths = []
	try:
		if e3 < 0:
			x = e3+x
			e3 = b5*e3
			x = 7*x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if e3 >= 9:
			x = b5-8
			paths.append(3)
		else:
			b5 = x-b5
			b5 = b5-4
			e3 = 9*e3
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		e3 = b5**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))