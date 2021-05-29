import numpy as np 

def function(x):

	m8 = 9
	g5 = x
	x = 3
	paths = []
	try:
		if m8 >= 6:
			m8 = 0-m8
			paths.append(1)
		else:
			g5 = g5*4
			g5 = g5-6
			paths.append(2)
		if g5 > 2:
			m8 = 6+m8
			paths.append(3)
		else:
			m8 = 6*x
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))