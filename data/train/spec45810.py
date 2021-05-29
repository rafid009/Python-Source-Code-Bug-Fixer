import numpy as np 

def function(x):

	j4 = 2
	y4 = 6
	paths = []
	try:
		if j4 >= 3:
			y4 = y4*1
			paths.append(1)
		else:
			y4 = y4-9
			y4 = 8*6
			y4 = y4/4
			paths.append(2)
		if x <= 3:
			x = 5/x
			j4 = j4*2
			y4 = 8/x
			paths.append(3)
		else:
			y4 = 9-j4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		j4 = y4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))