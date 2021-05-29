import numpy as np 

def function(x):

	y4 = 3
	j3 = 9
	paths = []
	try:
		if x < 1:
			j3 = 3-1
			paths.append(1)
		else:
			j3 = 3+j3
			j3 = j3-8
			paths.append(2)
		if y4 <= 2:
			x = 2+5
			paths.append(3)
		else:
			y4 = y4/x
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))