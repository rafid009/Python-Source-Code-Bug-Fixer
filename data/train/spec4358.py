import numpy as np 

def function(x):

	g1 = 6
	m4 = x
	paths = []
	try:
		if x <= 1:
			m4 = x*3
			g1 = 1*4
			x = x-x
			paths.append(1)
		else:
			x = 2+4
			paths.append(2)
		if g1 >= 4:
			x = g1-4
			paths.append(3)
		else:
			x = 6*1
			x = x+0
			x = 2*8
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