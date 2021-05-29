import numpy as np 

def function(x):

	j4 = 4
	g4 = x
	paths = []
	try:
		if j4 <= 2:
			j4 = j4-0
			paths.append(1)
		else:
			x = j4-x
			j4 = j4+x
			paths.append(2)
		if g4 < 1:
			j4 = 8-j4
			j4 = x/j4
			x = 7+0
			paths.append(3)
		else:
			j4 = g4/j4
			j4 = j4-3
			x = x+4
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