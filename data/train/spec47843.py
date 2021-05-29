import numpy as np 

def function(x):

	e3 = 3
	o9 = 8
	paths = []
	try:
		if o9 <= 4:
			e3 = e3+9
			e3 = x+7
			o9 = o9/e3
			paths.append(1)
		else:
			o9 = 2*o9
			x = 8+x
			o9 = o9*o9
			paths.append(2)
		if e3 < 4:
			e3 = e3+e3
			paths.append(3)
		else:
			o9 = e3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))