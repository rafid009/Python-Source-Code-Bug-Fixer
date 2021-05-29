import numpy as np 

def function(x):

	j1 = 7
	m0 = x
	paths = []
	try:
		if x < 3:
			x = 8+x
			x = x-6
			m0 = x*8
			paths.append(1)
		else:
			j1 = 0-4
			paths.append(2)
		if x <= 2:
			x = j1*j1
			paths.append(3)
		else:
			x = m0*8
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		m0 = m0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))