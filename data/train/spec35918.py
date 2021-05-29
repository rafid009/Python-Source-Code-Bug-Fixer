import numpy as np 

def function(x):

	a0 = x
	m1 = 1
	paths = []
	try:
		if a0 <= 8:
			x = x/9
			paths.append(1)
		else:
			a0 = m1+x
			paths.append(2)
		if m1 <= 2:
			m1 = a0-m1
			a0 = m1+1
			paths.append(3)
		else:
			x = 2/x
			x = x/x
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