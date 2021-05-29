import numpy as np 

def function(x):

	v1 = x
	m3 = 7
	paths = []
	try:
		if v1 > 4:
			x = 9*x
			paths.append(1)
		else:
			m3 = 6-m3
			paths.append(2)
		if x < 1:
			m3 = m3*m3
			paths.append(3)
		else:
			v1 = v1*v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))