import numpy as np 

def function(x):

	m3 = 7
	z5 = x
	paths = []
	try:
		if z5 > 9:
			m3 = 2+2
			paths.append(1)
		else:
			m3 = 1/3
			paths.append(2)
		if m3 >= 0:
			x = z5+x
			x = x-x
			paths.append(3)
		else:
			x = x-x
			x = 4-x
			x = x-x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		m3 = z5**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))