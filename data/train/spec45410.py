import numpy as np 

def function(x):

	n6 = 8
	m8 = 6
	paths = []
	try:
		if m8 > 2:
			m8 = 3*x
			m8 = m8+n6
			m8 = m8*5
			paths.append(1)
		else:
			x = x+x
			n6 = n6/n6
			n6 = n6*n6
			paths.append(2)
		if x > 1:
			n6 = n6*n6
			n6 = 9+7
			paths.append(3)
		else:
			n6 = 1/n6
			n6 = 1/m8
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		m8 = n6**0.5
		return m8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))