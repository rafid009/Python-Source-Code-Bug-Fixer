import numpy as np 

def function(x):

	j9 = 3
	y4 = x
	paths = []
	try:
		if x < 8:
			j9 = j9*1
			x = x+5
			x = j9*x
			paths.append(1)
		else:
			x = j9+2
			x = 0/4
			x = j9/5
			paths.append(2)
		if x >= 4:
			j9 = j9/y4
			x = x+6
			paths.append(3)
		else:
			j9 = j9+5
			y4 = y4*y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))