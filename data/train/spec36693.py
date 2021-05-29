import numpy as np 

def function(x):

	m0 = x
	o1 = x
	paths = []
	try:
		if x >= 2:
			m0 = 6*m0
			o1 = o1+o1
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if o1 < 7:
			m0 = m0-1
			paths.append(3)
		else:
			x = 7/x
			o1 = o1-4
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))