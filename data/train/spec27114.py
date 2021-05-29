import numpy as np 

def function(x):

	m0 = 2
	i0 = 5
	paths = []
	try:
		if m0 >= 9:
			i0 = 2/m0
			i0 = i0*5
			m0 = 7/m0
			paths.append(1)
		else:
			i0 = i0*i0
			i0 = 0+1
			paths.append(2)
		if x > 8:
			i0 = 2-3
			paths.append(3)
		else:
			i0 = 5-i0
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