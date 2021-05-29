import numpy as np 

def function(x):

	j2 = 5
	y4 = x
	paths = []
	try:
		if y4 >= 8:
			y4 = y4/x
			paths.append(1)
		else:
			j2 = j2+4
			paths.append(2)
		if j2 > 9:
			y4 = y4/2
			paths.append(3)
		else:
			j2 = 8-y4
			j2 = j2/j2
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))