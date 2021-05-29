import numpy as np 

def function(x):

	g1 = x
	b1 = 9
	paths = []
	try:
		if g1 < 4:
			g1 = g1-9
			g1 = g1-x
			b1 = x+x
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if b1 <= 3:
			b1 = 7+x
			paths.append(3)
		else:
			g1 = g1+5
			x = 8*4
			x = x-3
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