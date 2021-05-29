import numpy as np 

def function(x):

	m4 = x
	e8 = x
	paths = []
	try:
		if e8 >= 9:
			x = e8-1
			e8 = e8/5
			paths.append(1)
		else:
			e8 = 5-1
			e8 = 8/8
			paths.append(2)
		if m4 <= 2:
			m4 = m4+m4
			m4 = m4*8
			e8 = e8/m4
			paths.append(3)
		else:
			m4 = 0/e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))