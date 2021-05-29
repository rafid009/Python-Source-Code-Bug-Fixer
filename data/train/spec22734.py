import numpy as np 

def function(x):

	e2 = x
	m7 = 9
	paths = []
	try:
		if x >= 7:
			m7 = m7/8
			m7 = m7-4
			paths.append(1)
		else:
			m7 = m7-5
			paths.append(2)
		if m7 <= 0:
			m7 = 0-m7
			m7 = x+m7
			e2 = e2+m7
			paths.append(3)
		else:
			x = x-0
			x = e2+8
			e2 = e2/x
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