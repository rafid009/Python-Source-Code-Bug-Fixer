import numpy as np 

def function(x):

	v7 = x
	m0 = x
	paths = []
	try:
		if x < 1:
			v7 = 4*v7
			x = 6*6
			paths.append(1)
		else:
			m0 = m0/5
			paths.append(2)
		if m0 < 4:
			m0 = m0+8
			m0 = 8-x
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		v7 = m0**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))