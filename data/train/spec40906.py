import numpy as np 

def function(x):

	m9 = x
	g9 = 1
	paths = []
	try:
		if m9 >= 8:
			x = 5*g9
			paths.append(1)
		else:
			x = 5+x
			m9 = 4-m9
			m9 = m9-5
			paths.append(2)
		if x >= 3:
			g9 = 0/8
			g9 = g9-5
			paths.append(3)
		else:
			g9 = g9+m9
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))