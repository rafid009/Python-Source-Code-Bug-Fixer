import numpy as np 

def function(x):

	m5 = x
	g1 = 2
	x = x
	paths = []
	try:
		if g1 <= 6:
			x = x+x
			x = x+0
			paths.append(1)
		else:
			x = x-0
			g1 = 4-8
			x = x*7
			paths.append(2)
		if g1 >= 6:
			x = x/m5
			g1 = 2-x
			x = x-6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))