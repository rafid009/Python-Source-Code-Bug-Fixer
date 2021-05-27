import numpy as np 

def function(x):

	m3 = x
	m0 = x
	paths = []
	try:
		if x < 2:
			m0 = m0+7
			paths.append(1)
		else:
			m3 = m3/2
			m0 = 9+x
			paths.append(2)
		if x >= 5:
			m0 = m0+0
			m3 = m3-m3
			x = x/x
			paths.append(3)
		else:
			m3 = m3+2
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))