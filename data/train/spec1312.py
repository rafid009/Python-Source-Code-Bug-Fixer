import numpy as np 

def function(x):

	y4 = 1
	j6 = x
	paths = []
	try:
		if y4 >= 9:
			y4 = y4*y4
			j6 = j6-4
			paths.append(1)
		else:
			y4 = 0*6
			y4 = x/6
			j6 = x+j6
			paths.append(2)
		if x < 3:
			j6 = x/j6
			paths.append(3)
		else:
			j6 = j6+y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))