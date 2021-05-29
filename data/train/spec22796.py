import numpy as np 

def function(x):

	k3 = x
	g4 = x
	paths = []
	try:
		if x > 5:
			k3 = k3+2
			k3 = 1-k3
			g4 = g4*x
			paths.append(1)
		else:
			g4 = g4/g4
			paths.append(2)
		if g4 <= 4:
			x = x+2
			paths.append(3)
		else:
			k3 = x+k3
			g4 = k3*k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))