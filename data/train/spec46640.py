import numpy as np 

def function(x):

	o9 = x
	m5 = x
	paths = []
	try:
		if x >= 0:
			x = 7+o9
			o9 = o9/6
			paths.append(1)
		else:
			o9 = o9+2
			m5 = o9/x
			o9 = o9*m5
			paths.append(2)
		if x >= 3:
			x = m5*o9
			paths.append(3)
		else:
			o9 = o9-5
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))