import numpy as np 

def function(x):

	i3 = x
	g0 = x
	paths = []
	try:
		if i3 >= 2:
			x = x/1
			i3 = i3/4
			paths.append(1)
		else:
			g0 = 1+7
			i3 = 0+i3
			paths.append(2)
		if x > 1:
			g0 = g0/7
			g0 = 7/i3
			paths.append(3)
		else:
			i3 = 6/i3
			i3 = i3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))