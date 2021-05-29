import numpy as np 

def function(x):

	b4 = x
	m9 = 8
	paths = []
	try:
		if b4 <= 9:
			m9 = 9*9
			paths.append(1)
		else:
			m9 = m9-9
			x = x/5
			b4 = 8-b4
			paths.append(2)
		if x < 2:
			b4 = b4/8
			m9 = 3-x
			paths.append(3)
		else:
			x = x*b4
			x = m9+x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))