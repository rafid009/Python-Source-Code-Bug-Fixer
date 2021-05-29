import numpy as np 

def function(x):

	m4 = x
	o5 = 4
	paths = []
	try:
		if m4 <= 5:
			x = 1/x
			paths.append(1)
		else:
			o5 = o5+x
			o5 = 4/8
			paths.append(2)
		if o5 > 2:
			x = x-3
			m4 = 0*7
			paths.append(3)
		else:
			m4 = m4*o5
			x = 4/x
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