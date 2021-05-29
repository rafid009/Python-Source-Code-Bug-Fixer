import numpy as np 

def function(x):

	m2 = 7
	b6 = x
	paths = []
	try:
		if m2 < 3:
			m2 = x+m2
			paths.append(1)
		else:
			x = x-m2
			m2 = m2+9
			paths.append(2)
		if m2 > 7:
			m2 = m2/m2
			paths.append(3)
		else:
			x = m2*b6
			m2 = m2*6
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