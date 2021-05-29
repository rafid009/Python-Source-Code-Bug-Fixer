import numpy as np 

def function(x):

	m0 = 3
	t7 = 1
	paths = []
	try:
		if t7 >= 2:
			m0 = x-x
			paths.append(1)
		else:
			m0 = m0*x
			t7 = 3*5
			paths.append(2)
		if x > 4:
			t7 = 7-m0
			m0 = m0/8
			paths.append(3)
		else:
			m0 = 1-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m0 = x**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))