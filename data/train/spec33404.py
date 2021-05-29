import numpy as np 

def function(x):

	g5 = 6
	k8 = 2
	paths = []
	try:
		if k8 >= 3:
			g5 = 3-g5
			k8 = k8-g5
			paths.append(1)
		else:
			k8 = x*3
			g5 = 8-x
			paths.append(2)
		if g5 <= 4:
			g5 = g5*3
			paths.append(3)
		else:
			k8 = 9/g5
			x = x+x
			g5 = 1+g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))