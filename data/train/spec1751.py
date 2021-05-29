import numpy as np 

def function(x):

	e0 = x
	m5 = 6
	paths = []
	try:
		if m5 >= 1:
			x = x-3
			m5 = m5-4
			paths.append(1)
		else:
			m5 = 2-m5
			paths.append(2)
		if e0 <= 8:
			m5 = 9-m5
			m5 = 3*m5
			m5 = 1-9
			paths.append(3)
		else:
			x = 6+3
			e0 = 8+5
			m5 = m5/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))