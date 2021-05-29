import numpy as np 

def function(x):

	u2 = x
	m9 = x
	paths = []
	try:
		if x >= 3:
			x = 8/x
			u2 = u2+9
			paths.append(1)
		else:
			m9 = x/2
			u2 = u2/6
			paths.append(2)
		if x < 3:
			x = m9-1
			x = m9*5
			x = m9+x
			paths.append(3)
		else:
			u2 = m9+1
			u2 = 2*x
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))