import numpy as np 

def function(x):

	f3 = x
	m0 = 4
	paths = []
	try:
		if m0 >= 0:
			x = 8*f3
			paths.append(1)
		else:
			x = x-0
			m0 = m0*6
			paths.append(2)
		if x < 2:
			x = 3+2
			m0 = 9*f3
			x = x+x
			paths.append(3)
		else:
			f3 = 3+f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))