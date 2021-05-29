import numpy as np 

def function(x):

	v1 = 5
	m7 = 7
	paths = []
	try:
		if x < 5:
			m7 = m7-6
			v1 = 3/m7
			x = x+1
			paths.append(1)
		else:
			m7 = v1-0
			paths.append(2)
		if x >= 3:
			x = x-4
			paths.append(3)
		else:
			x = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))