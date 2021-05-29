import numpy as np 

def function(x):

	i0 = x
	m4 = 1
	paths = []
	try:
		if m4 >= 6:
			i0 = 5/8
			m4 = m4*m4
			paths.append(1)
		else:
			i0 = i0-i0
			x = x/3
			paths.append(2)
		if m4 > 2:
			m4 = m4*x
			m4 = i0+9
			paths.append(3)
		else:
			i0 = 2*x
			m4 = 7*m4
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