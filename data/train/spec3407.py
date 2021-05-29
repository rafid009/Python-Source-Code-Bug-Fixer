import numpy as np 

def function(x):

	j4 = x
	y8 = x
	x = 2
	paths = []
	try:
		if x > 7:
			y8 = y8/7
			j4 = j4*4
			paths.append(1)
		else:
			y8 = 1+7
			y8 = y8-7
			x = 6+4
			paths.append(2)
		if j4 < 6:
			x = 2/4
			y8 = 6+y8
			paths.append(3)
		else:
			y8 = y8+9
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))