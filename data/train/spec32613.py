import numpy as np 

def function(x):

	i7 = x
	g1 = 1
	paths = []
	try:
		if g1 < 2:
			i7 = i7*9
			paths.append(1)
		else:
			x = x*9
			g1 = g1*1
			paths.append(2)
		if i7 > 4:
			i7 = i7-2
			x = i7*x
			paths.append(3)
		else:
			i7 = i7*9
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))