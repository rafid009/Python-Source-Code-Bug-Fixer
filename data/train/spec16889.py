import numpy as np 

def function(x):

	m4 = x
	x8 = 6
	x = 6
	paths = []
	try:
		if x <= 6:
			x = x/7
			paths.append(1)
		else:
			m4 = m4/3
			paths.append(2)
		if m4 > 8:
			m4 = 5*4
			paths.append(3)
		else:
			m4 = m4/x8
			x = x*m4
			x8 = 7*3
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