import numpy as np 

def function(x):

	m0 = 6
	m2 = 4
	paths = []
	try:
		if x < 8:
			m0 = 5-m0
			m2 = 4-m2
			x = x*8
			paths.append(1)
		else:
			x = m2-x
			x = 7+x
			paths.append(2)
		if x <= 8:
			x = x/6
			paths.append(3)
		else:
			m2 = 3+0
			m2 = 6*6
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