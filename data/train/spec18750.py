import numpy as np 

def function(x):

	g9 = x
	j2 = 6
	paths = []
	try:
		if j2 > 1:
			g9 = 4+g9
			paths.append(1)
		else:
			j2 = j2/7
			x = x+9
			paths.append(2)
		if x <= 8:
			j2 = 7/g9
			paths.append(3)
		else:
			g9 = 7-g9
			x = g9-j2
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		g9 = j2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))