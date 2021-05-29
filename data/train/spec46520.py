import numpy as np 

def function(x):

	g1 = x
	i0 = 2
	x = x
	paths = []
	try:
		if i0 > 7:
			i0 = i0/8
			i0 = 0*g1
			x = x/1
			paths.append(1)
		else:
			x = i0*9
			g1 = 7/g1
			g1 = g1*7
			paths.append(2)
		if g1 <= 2:
			g1 = g1-i0
			i0 = i0-8
			x = x-g1
			paths.append(3)
		else:
			i0 = x/i0
			g1 = g1/2
			i0 = 7/i0
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