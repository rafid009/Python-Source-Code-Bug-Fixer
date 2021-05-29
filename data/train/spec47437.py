import numpy as np 

def function(x):

	y4 = 4
	i1 = x
	x = 4
	paths = []
	try:
		if y4 <= 5:
			i1 = i1*6
			paths.append(1)
		else:
			i1 = i1/2
			paths.append(2)
		if y4 < 7:
			y4 = y4-2
			x = x*7
			paths.append(3)
		else:
			x = x-x
			i1 = i1-9
			y4 = y4+4
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))