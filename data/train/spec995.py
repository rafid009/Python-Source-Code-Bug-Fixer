import numpy as np 

def function(x):

	t4 = x
	m0 = 1
	x = x
	paths = []
	try:
		if m0 >= 6:
			t4 = 8+m0
			paths.append(1)
		else:
			m0 = t4+m0
			m0 = m0/2
			paths.append(2)
		if m0 < 2:
			x = x/3
			x = x/6
			m0 = m0+6
			paths.append(3)
		else:
			m0 = m0*t4
			x = x/x
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