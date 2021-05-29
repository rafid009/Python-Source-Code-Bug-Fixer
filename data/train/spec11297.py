import numpy as np 

def function(x):

	i0 = 3
	m1 = 5
	paths = []
	try:
		if i0 > 1:
			i0 = 2*3
			paths.append(1)
		else:
			i0 = i0-5
			m1 = 1+6
			paths.append(2)
		if x >= 6:
			i0 = 6*i0
			x = x*3
			i0 = 0+8
			paths.append(3)
		else:
			m1 = m1/i0
			i0 = i0-9
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		m1 = i0**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))