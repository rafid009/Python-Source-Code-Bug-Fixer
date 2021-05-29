import numpy as np 

def function(x):

	m2 = x
	v9 = 5
	paths = []
	try:
		if v9 <= 2:
			m2 = 9*1
			paths.append(1)
		else:
			v9 = 8+v9
			x = x-6
			v9 = v9/m2
			paths.append(2)
		if x < 0:
			m2 = 1-m2
			x = x-5
			paths.append(3)
		else:
			m2 = 6/m2
			v9 = v9+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m2 = x**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))