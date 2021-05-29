import numpy as np 

def function(x):

	m4 = x
	g1 = 4
	x = x
	paths = []
	try:
		if g1 > 4:
			x = x*x
			g1 = m4/1
			paths.append(1)
		else:
			g1 = m4-0
			x = x/m4
			g1 = g1-2
			paths.append(2)
		if g1 <= 0:
			x = x/2
			x = g1-x
			paths.append(3)
		else:
			g1 = g1+9
			g1 = g1*8
			g1 = g1+2
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))