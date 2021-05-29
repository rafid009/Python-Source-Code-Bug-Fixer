import numpy as np 

def function(x):

	e9 = x
	t8 = x
	paths = []
	try:
		if x <= 5:
			x = x*5
			t8 = e9/t8
			e9 = x+5
			paths.append(1)
		else:
			t8 = t8/3
			e9 = x-2
			e9 = 4*e9
			paths.append(2)
		if x >= 2:
			x = e9*4
			paths.append(3)
		else:
			t8 = 9-2
			e9 = e9-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))