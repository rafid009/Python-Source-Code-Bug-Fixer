import numpy as np 

def function(x):

	m1 = x
	d5 = 8
	paths = []
	try:
		if d5 >= 7:
			m1 = m1+4
			m1 = m1+3
			paths.append(1)
		else:
			d5 = d5*6
			paths.append(2)
		if m1 <= 3:
			d5 = d5*m1
			m1 = x+4
			paths.append(3)
		else:
			x = x-x
			m1 = d5/m1
			m1 = m1-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))