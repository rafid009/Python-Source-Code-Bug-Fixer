import numpy as np 

def function(x):

	g8 = x
	k9 = 3
	x = x
	paths = []
	try:
		if x < 8:
			x = x+1
			x = 2*7
			k9 = k9*7
			paths.append(1)
		else:
			g8 = g8-1
			x = x*7
			paths.append(2)
		if x <= 6:
			x = x+7
			paths.append(3)
		else:
			k9 = k9*4
			k9 = k9*k9
			k9 = 0+0
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))