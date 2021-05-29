import numpy as np 

def function(x):

	x1 = x
	m2 = x
	paths = []
	try:
		if x1 > 1:
			x1 = 3/5
			m2 = m2-7
			x1 = x1+x1
			paths.append(1)
		else:
			m2 = m2/3
			m2 = m2*7
			paths.append(2)
		if m2 > 1:
			x1 = 4/x1
			x1 = 2/x1
			paths.append(3)
		else:
			m2 = m2/4
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		m2 = m2**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))