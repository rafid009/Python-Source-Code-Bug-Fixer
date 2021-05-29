import numpy as np 

def function(x):

	e9 = 8
	o4 = 8
	x = 5
	paths = []
	try:
		if x > 1:
			x = 4-8
			o4 = o4-x
			e9 = 8/e9
			paths.append(1)
		else:
			e9 = o4+3
			x = x*e9
			paths.append(2)
		if e9 <= 1:
			o4 = o4/o4
			e9 = e9-2
			x = 3/x
			paths.append(3)
		else:
			e9 = e9/x
			paths.append(4)
		paths.append(5)
		assert e9 >= 0
		x = e9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))