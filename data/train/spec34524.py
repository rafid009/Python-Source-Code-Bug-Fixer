import numpy as np 

def function(x):

	m1 = x
	d4 = x
	paths = []
	try:
		if d4 > 4:
			m1 = m1+8
			paths.append(1)
		else:
			x = 5*9
			paths.append(2)
		if m1 <= 5:
			x = 3-x
			m1 = m1/9
			paths.append(3)
		else:
			d4 = d4-x
			d4 = d4-4
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		m1 = d4**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))