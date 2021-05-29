import numpy as np 

def function(x):

	m1 = 1
	v9 = x
	x = x
	paths = []
	try:
		if m1 < 5:
			m1 = 9*2
			x = v9-5
			x = 3/x
			paths.append(1)
		else:
			x = v9*2
			m1 = 8+0
			m1 = 1/1
			paths.append(2)
		if x >= 8:
			v9 = v9*v9
			m1 = v9+m1
			x = 8+m1
			paths.append(3)
		else:
			v9 = 9/3
			m1 = m1/6
			m1 = v9*m1
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