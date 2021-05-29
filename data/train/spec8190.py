import numpy as np 

def function(x):

	m3 = x
	n5 = 3
	paths = []
	try:
		if n5 < 2:
			m3 = m3/n5
			m3 = 8/5
			paths.append(1)
		else:
			x = 1-n5
			n5 = 7*m3
			m3 = 6*m3
			paths.append(2)
		if x < 7:
			n5 = 1+n5
			paths.append(3)
		else:
			n5 = n5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))