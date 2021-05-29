import numpy as np 

def function(x):

	i0 = x
	m6 = 5
	paths = []
	try:
		if i0 < 1:
			m6 = 3/i0
			i0 = 4*3
			paths.append(1)
		else:
			m6 = 2+m6
			x = x+5
			i0 = i0*i0
			paths.append(2)
		if x <= 2:
			m6 = m6/i0
			paths.append(3)
		else:
			m6 = m6-m6
			i0 = i0-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i0 = x**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))