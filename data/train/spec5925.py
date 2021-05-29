import numpy as np 

def function(x):

	m4 = x
	a7 = x
	paths = []
	try:
		if m4 > 9:
			x = x+3
			x = x+4
			x = 7/x
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if x > 4:
			m4 = 4-6
			paths.append(3)
		else:
			x = 9+4
			m4 = m4/m4
			x = x-a7
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))