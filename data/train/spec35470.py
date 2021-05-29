import numpy as np 

def function(x):

	m6 = 4
	d2 = x
	paths = []
	try:
		if d2 >= 9:
			m6 = m6-8
			d2 = d2*5
			x = 4+7
			paths.append(1)
		else:
			x = 7/m6
			d2 = 1*d2
			paths.append(2)
		if d2 > 4:
			m6 = m6-d2
			paths.append(3)
		else:
			m6 = 5-m6
			d2 = m6*8
			d2 = d2-8
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))