import numpy as np 

def function(x):

	m1 = 0
	g1 = x
	paths = []
	try:
		if x <= 0:
			m1 = g1+1
			m1 = 4-m1
			paths.append(1)
		else:
			x = 3-m1
			paths.append(2)
		if x > 4:
			x = x*g1
			m1 = 5-5
			paths.append(3)
		else:
			g1 = g1-m1
			g1 = 6*g1
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))