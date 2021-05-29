import numpy as np 

def function(x):

	d5 = x
	m2 = 1
	paths = []
	try:
		if d5 >= 6:
			m2 = 3/x
			m2 = 0*x
			paths.append(1)
		else:
			m2 = m2+x
			paths.append(2)
		if m2 > 4:
			x = 9-9
			m2 = m2-4
			m2 = d5/m2
			paths.append(3)
		else:
			x = x-9
			m2 = m2-m2
			x = m2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))