import numpy as np 

def function(x):

	e3 = 7
	f4 = x
	paths = []
	try:
		if f4 <= 1:
			x = x*4
			paths.append(1)
		else:
			x = 2*f4
			e3 = 6/e3
			x = f4/f4
			paths.append(2)
		if e3 < 7:
			x = 7-4
			e3 = 5*f4
			e3 = 4-e3
			paths.append(3)
		else:
			x = 3+6
			x = 5+2
			f4 = 7-8
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