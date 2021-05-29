import numpy as np 

def function(x):

	f8 = x
	e1 = x
	paths = []
	try:
		if x <= 0:
			x = x+9
			x = x/6
			e1 = 6/7
			paths.append(1)
		else:
			e1 = e1/f8
			paths.append(2)
		if x >= 6:
			f8 = f8+8
			x = x-5
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))