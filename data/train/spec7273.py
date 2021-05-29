import numpy as np 

def function(x):

	k1 = 7
	m6 = 1
	paths = []
	try:
		if k1 < 8:
			m6 = m6-3
			paths.append(1)
		else:
			k1 = k1-m6
			m6 = m6-5
			m6 = m6-x
			paths.append(2)
		if m6 <= 9:
			k1 = k1-x
			paths.append(3)
		else:
			x = x+1
			m6 = 2/m6
			x = 0+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))