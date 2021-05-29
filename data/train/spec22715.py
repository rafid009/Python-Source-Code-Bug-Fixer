import numpy as np 

def function(x):

	i0 = x
	m7 = x
	paths = []
	try:
		if i0 >= 5:
			m7 = m7/2
			m7 = m7-i0
			i0 = 8*7
			paths.append(1)
		else:
			i0 = i0-2
			paths.append(2)
		if x < 8:
			i0 = i0*i0
			paths.append(3)
		else:
			m7 = m7-x
			x = i0-3
			i0 = m7+2
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))