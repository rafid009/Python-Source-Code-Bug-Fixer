import numpy as np 

def function(x):

	o5 = 1
	m4 = x
	paths = []
	try:
		if o5 < 4:
			o5 = o5-x
			m4 = 5-x
			paths.append(1)
		else:
			o5 = x*o5
			paths.append(2)
		if o5 <= 9:
			x = 2-x
			paths.append(3)
		else:
			x = 8/o5
			x = 5/x
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))