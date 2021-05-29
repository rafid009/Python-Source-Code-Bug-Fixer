import numpy as np 

def function(x):

	g0 = x
	i3 = 6
	paths = []
	try:
		if x >= 7:
			i3 = 0*i3
			i3 = 4/4
			x = g0/4
			paths.append(1)
		else:
			i3 = 3*6
			x = x/9
			paths.append(2)
		if i3 <= 3:
			g0 = g0/g0
			x = 9+5
			paths.append(3)
		else:
			i3 = 5-0
			x = i3/8
			paths.append(4)
		paths.append(5)
		assert g0 >= 0
		g0 = g0**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))