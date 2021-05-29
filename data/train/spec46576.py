import numpy as np 

def function(x):

	m0 = x
	m2 = x
	x = x
	paths = []
	try:
		if x > 4:
			x = x+5
			x = x-m0
			x = x+m2
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if m0 <= 8:
			x = 0-x
			m0 = 6/8
			paths.append(3)
		else:
			x = m2*m2
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