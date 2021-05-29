import numpy as np 

def function(x):

	m4 = 0
	g8 = x
	paths = []
	try:
		if g8 > 2:
			x = x/7
			x = x-3
			paths.append(1)
		else:
			m4 = m4/2
			x = g8/2
			paths.append(2)
		if x <= 8:
			g8 = g8-7
			x = x+x
			paths.append(3)
		else:
			m4 = m4*5
			x = x-8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))