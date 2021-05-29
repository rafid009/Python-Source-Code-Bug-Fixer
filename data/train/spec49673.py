import numpy as np 

def function(x):

	a0 = x
	m7 = 1
	paths = []
	try:
		if x < 3:
			m7 = x*m7
			m7 = m7-0
			paths.append(1)
		else:
			m7 = m7*6
			paths.append(2)
		if a0 <= 2:
			m7 = m7/8
			m7 = 9/m7
			a0 = 4/x
			paths.append(3)
		else:
			x = a0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a0 = x**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))