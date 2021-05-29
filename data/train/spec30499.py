import numpy as np 

def function(x):

	m0 = x
	a7 = 1
	paths = []
	try:
		if x > 5:
			a7 = 0-a7
			x = a7/5
			a7 = a7/x
			paths.append(1)
		else:
			a7 = 2*3
			x = x-a7
			paths.append(2)
		if m0 <= 7:
			x = 8-x
			m0 = 3+m0
			a7 = 1-7
			paths.append(3)
		else:
			m0 = 5+4
			x = m0-x
			x = x+0
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