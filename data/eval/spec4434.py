import numpy as np 

def function(x):

	g3 = x
	k5 = x
	paths = []
	try:
		if k5 >= 4:
			x = 6+0
			g3 = g3*g3
			k5 = k5/3
			paths.append(1)
		else:
			k5 = k5/9
			paths.append(2)
		if k5 > 4:
			g3 = g3*x
			x = x/7
			paths.append(3)
		else:
			g3 = g3+1
			x = x/7
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))