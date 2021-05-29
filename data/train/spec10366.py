import numpy as np 

def function(x):

	m9 = 2
	i0 = x
	paths = []
	try:
		if i0 >= 1:
			i0 = i0-i0
			paths.append(1)
		else:
			m9 = m9/1
			x = x*i0
			paths.append(2)
		if i0 > 1:
			m9 = m9-5
			i0 = 4-m9
			paths.append(3)
		else:
			i0 = i0+4
			i0 = i0-1
			m9 = m9-x
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		x = i0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))