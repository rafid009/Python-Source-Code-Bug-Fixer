import numpy as np 

def function(x):

	g0 = x
	i5 = x
	paths = []
	try:
		if x > 3:
			g0 = g0*1
			g0 = g0+4
			paths.append(1)
		else:
			x = g0/3
			i5 = i5-g0
			i5 = 7-i5
			paths.append(2)
		if x > 6:
			x = x+i5
			paths.append(3)
		else:
			g0 = x*7
			i5 = i5-4
			x = x-4
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		x = i5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))