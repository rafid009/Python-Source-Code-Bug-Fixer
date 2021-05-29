import numpy as np 

def function(x):

	i4 = x
	m8 = x
	paths = []
	try:
		if m8 > 5:
			x = m8+i4
			x = x+x
			paths.append(1)
		else:
			i4 = x-7
			x = 4-9
			x = x/8
			paths.append(2)
		if x >= 6:
			i4 = 9*4
			paths.append(3)
		else:
			i4 = 2*i4
			m8 = 0/m8
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