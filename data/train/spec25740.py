import numpy as np 

def function(x):

	g4 = x
	j4 = x
	paths = []
	try:
		if j4 <= 9:
			x = 1-x
			paths.append(1)
		else:
			j4 = j4+5
			paths.append(2)
		if x <= 0:
			g4 = x*2
			paths.append(3)
		else:
			g4 = 5+4
			x = x+5
			g4 = 0+g4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))