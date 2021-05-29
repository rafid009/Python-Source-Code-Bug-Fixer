import numpy as np 

def function(x):

	a0 = 1
	m1 = 6
	paths = []
	try:
		if x > 6:
			m1 = m1/x
			paths.append(1)
		else:
			m1 = 6+9
			m1 = 9/m1
			paths.append(2)
		if a0 >= 8:
			a0 = 8*a0
			a0 = a0/4
			m1 = m1/2
			paths.append(3)
		else:
			m1 = m1-a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))