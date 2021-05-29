import numpy as np 

def function(x):

	g8 = 4
	j1 = x
	paths = []
	try:
		if x <= 5:
			j1 = j1+7
			paths.append(1)
		else:
			j1 = j1-0
			paths.append(2)
		if g8 < 3:
			g8 = g8-1
			paths.append(3)
		else:
			j1 = 3*g8
			j1 = 9-j1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))