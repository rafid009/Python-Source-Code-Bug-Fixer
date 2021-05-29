import numpy as np 

def function(x):

	k9 = 7
	g9 = 9
	x = x
	paths = []
	try:
		if x <= 2:
			x = k9*k9
			k9 = k9+2
			paths.append(1)
		else:
			g9 = g9-5
			g9 = 8+7
			paths.append(2)
		if x <= 9:
			x = x+2
			g9 = 9*g9
			paths.append(3)
		else:
			k9 = k9/8
			k9 = k9-x
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))