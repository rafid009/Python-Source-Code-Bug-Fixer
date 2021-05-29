import numpy as np 

def function(x):

	f4 = x
	e0 = 9
	paths = []
	try:
		if e0 >= 7:
			f4 = 1+f4
			e0 = 5-3
			paths.append(1)
		else:
			e0 = e0+6
			x = 6+x
			paths.append(2)
		if f4 <= 1:
			e0 = 4*e0
			x = 4+x
			e0 = e0-9
			paths.append(3)
		else:
			f4 = 4*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))