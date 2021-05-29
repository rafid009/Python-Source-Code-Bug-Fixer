import numpy as np 

def function(x):

	m7 = 9
	v4 = 5
	paths = []
	try:
		if m7 > 2:
			x = x*v4
			x = 3/x
			m7 = 4-1
			paths.append(1)
		else:
			x = x-9
			v4 = m7-v4
			x = v4+x
			paths.append(2)
		if x <= 3:
			x = 1/x
			paths.append(3)
		else:
			x = 5/x
			m7 = 0*9
			x = v4*x
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