import numpy as np 

def function(x):

	m0 = x
	n4 = x
	paths = []
	try:
		if n4 < 4:
			n4 = 6+n4
			paths.append(1)
		else:
			m0 = 1+m0
			x = x-9
			n4 = m0-n4
			paths.append(2)
		if m0 >= 6:
			n4 = n4-6
			n4 = 4/9
			m0 = 2*x
			paths.append(3)
		else:
			m0 = n4/m0
			x = 8+8
			m0 = 6-7
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