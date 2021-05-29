import numpy as np 

def function(x):

	g0 = 9
	m4 = 5
	paths = []
	try:
		if x <= 7:
			x = x-6
			paths.append(1)
		else:
			g0 = m4+g0
			m4 = x-m4
			g0 = x*g0
			paths.append(2)
		if g0 >= 7:
			x = x+g0
			x = m4/6
			m4 = m4-g0
			paths.append(3)
		else:
			m4 = 0/8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))