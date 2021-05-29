import numpy as np 

def function(x):

	g4 = 8
	k7 = x
	x = x
	paths = []
	try:
		if k7 >= 6:
			g4 = 7-8
			k7 = 2-9
			k7 = k7-5
			paths.append(1)
		else:
			k7 = 0+k7
			paths.append(2)
		if x <= 8:
			k7 = 5/9
			k7 = k7-k7
			paths.append(3)
		else:
			g4 = k7+9
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))