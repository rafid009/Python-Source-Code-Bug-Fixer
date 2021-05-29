import numpy as np 

def function(x):

	i3 = 5
	g1 = x
	paths = []
	try:
		if g1 <= 2:
			i3 = i3+8
			x = x-2
			i3 = i3*6
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if i3 > 3:
			g1 = g1-4
			g1 = 2*g1
			x = 3/x
			paths.append(3)
		else:
			i3 = i3+0
			x = g1-8
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