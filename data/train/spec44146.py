import numpy as np 

def function(x):

	o4 = x
	m0 = 4
	x = x
	paths = []
	try:
		if o4 >= 7:
			x = x*7
			x = x/o4
			m0 = m0+m0
			paths.append(1)
		else:
			m0 = m0+x
			m0 = 2+6
			m0 = o4/m0
			paths.append(2)
		if m0 < 8:
			x = x*5
			o4 = 3+o4
			paths.append(3)
		else:
			o4 = 6-o4
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