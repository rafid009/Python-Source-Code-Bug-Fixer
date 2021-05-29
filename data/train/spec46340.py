import numpy as np 

def function(x):

	m4 = x
	b6 = 1
	paths = []
	try:
		if x <= 5:
			m4 = m4-3
			paths.append(1)
		else:
			x = x-4
			x = x+2
			paths.append(2)
		if m4 >= 7:
			b6 = 1*b6
			x = x/x
			b6 = 8-b6
			paths.append(3)
		else:
			m4 = m4*3
			m4 = b6+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))