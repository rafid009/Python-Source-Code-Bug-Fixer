import numpy as np 

def function(x):

	v7 = x
	g1 = 1
	paths = []
	try:
		if x > 7:
			v7 = 8/g1
			v7 = g1+7
			g1 = 0+x
			paths.append(1)
		else:
			g1 = g1*7
			g1 = 5-g1
			paths.append(2)
		if x < 2:
			v7 = v7-v7
			paths.append(3)
		else:
			x = g1+x
			g1 = 8/1
			v7 = 0-v7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		v7 = g1**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))