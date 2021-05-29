import numpy as np 

def function(x):

	v2 = 5
	m3 = x
	paths = []
	try:
		if v2 < 2:
			x = 8+x
			paths.append(1)
		else:
			m3 = m3+7
			paths.append(2)
		if x < 0:
			m3 = 9+5
			paths.append(3)
		else:
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))