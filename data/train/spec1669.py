import numpy as np 

def function(x):

	m0 = 6
	k7 = x
	paths = []
	try:
		if x > 3:
			x = 8+x
			m0 = 3+m0
			paths.append(1)
		else:
			x = 2+x
			x = k7/x
			paths.append(2)
		if k7 >= 3:
			m0 = 5*m0
			m0 = 0+5
			paths.append(3)
		else:
			k7 = k7/2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		m0 = k7**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))