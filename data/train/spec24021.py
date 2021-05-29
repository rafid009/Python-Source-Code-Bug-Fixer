import numpy as np 

def function(x):

	m0 = x
	g4 = x
	paths = []
	try:
		if x > 5:
			x = g4/9
			g4 = g4*5
			x = x+g4
			paths.append(1)
		else:
			g4 = g4+1
			paths.append(2)
		if g4 > 1:
			m0 = m0*2
			g4 = g4-m0
			paths.append(3)
		else:
			g4 = m0+g4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))