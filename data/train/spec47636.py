import numpy as np 

def function(x):

	m0 = x
	r8 = x
	paths = []
	try:
		if m0 > 4:
			x = 2*4
			m0 = 7-x
			paths.append(1)
		else:
			m0 = m0/4
			paths.append(2)
		if x >= 4:
			r8 = m0-m0
			m0 = m0+r8
			paths.append(3)
		else:
			r8 = 4/3
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))