import numpy as np 

def function(x):

	e4 = 4
	f3 = 7
	x = x
	paths = []
	try:
		if f3 < 7:
			x = x*0
			x = x-8
			paths.append(1)
		else:
			e4 = 5/e4
			e4 = 4*f3
			f3 = x-f3
			paths.append(2)
		if x >= 3:
			e4 = e4+9
			e4 = e4+f3
			paths.append(3)
		else:
			f3 = f3-f3
			e4 = e4/8
			f3 = f3+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))