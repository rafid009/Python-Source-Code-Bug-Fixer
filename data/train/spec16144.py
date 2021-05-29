import numpy as np 

def function(x):

	o1 = x
	m3 = x
	paths = []
	try:
		if x < 2:
			o1 = 4*6
			o1 = 8+o1
			paths.append(1)
		else:
			m3 = o1/5
			x = o1*x
			paths.append(2)
		if o1 > 0:
			m3 = 8-m3
			x = 6*x
			paths.append(3)
		else:
			m3 = m3+3
			m3 = 8*x
			o1 = 6-o1
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