import numpy as np 

def function(x):

	e3 = 3
	m5 = x
	paths = []
	try:
		if m5 >= 0:
			m5 = m5-4
			x = 3/x
			paths.append(1)
		else:
			e3 = e3*6
			m5 = 0-6
			paths.append(2)
		if e3 >= 7:
			x = x/5
			paths.append(3)
		else:
			x = 3-x
			e3 = e3*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m5 = x**0.5
		return m5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))