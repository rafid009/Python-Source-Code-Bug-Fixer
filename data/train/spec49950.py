import numpy as np 

def function(x):

	i0 = x
	m6 = 8
	paths = []
	try:
		if i0 <= 7:
			m6 = 1*8
			paths.append(1)
		else:
			i0 = 6+m6
			paths.append(2)
		if i0 >= 1:
			i0 = i0+2
			i0 = i0-2
			m6 = 1+m6
			paths.append(3)
		else:
			x = x*5
			m6 = 2-6
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		m6 = i0**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))