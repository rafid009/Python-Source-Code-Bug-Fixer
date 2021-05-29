import numpy as np 

def function(x):

	n5 = x
	m6 = 0
	x = 8
	paths = []
	try:
		if x >= 8:
			m6 = m6*3
			x = 0*8
			paths.append(1)
		else:
			n5 = 9+0
			paths.append(2)
		if n5 >= 4:
			m6 = m6+7
			n5 = n5-8
			m6 = m6*x
			paths.append(3)
		else:
			n5 = 4/4
			x = 4*x
			n5 = n5+n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		m6 = n5**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))