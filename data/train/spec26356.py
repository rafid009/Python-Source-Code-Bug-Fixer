import numpy as np 

def function(x):

	m4 = x
	m3 = 4
	paths = []
	try:
		if m3 > 3:
			m4 = 5/1
			x = x-9
			paths.append(1)
		else:
			m4 = 3-m4
			paths.append(2)
		if m4 < 0:
			m3 = 5+5
			paths.append(3)
		else:
			m4 = m4/1
			m3 = 6/5
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