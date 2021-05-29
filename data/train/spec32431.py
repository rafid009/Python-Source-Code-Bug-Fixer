import numpy as np 

def function(x):

	k1 = 1
	g4 = x
	paths = []
	try:
		if g4 <= 8:
			g4 = x-1
			g4 = g4/k1
			x = 5/g4
			paths.append(1)
		else:
			x = x/3
			g4 = x+g4
			g4 = x*3
			paths.append(2)
		if x > 7:
			g4 = g4+3
			paths.append(3)
		else:
			x = x-6
			x = x+k1
			k1 = k1-g4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))