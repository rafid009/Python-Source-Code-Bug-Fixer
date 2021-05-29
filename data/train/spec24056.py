import numpy as np 

def function(x):

	n9 = 4
	m2 = x
	paths = []
	try:
		if m2 <= 4:
			x = 7*2
			paths.append(1)
		else:
			x = n9+6
			m2 = 2+3
			x = 2-m2
			paths.append(2)
		if m2 > 4:
			n9 = m2*x
			paths.append(3)
		else:
			m2 = n9/m2
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