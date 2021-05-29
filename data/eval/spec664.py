import numpy as np 

def function(x):

	k8 = x
	g7 = 2
	paths = []
	try:
		if g7 > 5:
			g7 = 2+5
			g7 = g7+0
			g7 = g7+g7
			paths.append(1)
		else:
			k8 = 7*k8
			x = 3*x
			x = x+3
			paths.append(2)
		if k8 < 5:
			g7 = 0/g7
			k8 = g7/k8
			g7 = 5*x
			paths.append(3)
		else:
			x = 2+1
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