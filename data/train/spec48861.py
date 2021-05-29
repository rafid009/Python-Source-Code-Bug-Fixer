import numpy as np 

def function(x):

	l8 = 6
	j4 = x
	x = x
	paths = []
	try:
		if x >= 7:
			j4 = j4*l8
			l8 = l8*2
			j4 = 4*8
			paths.append(1)
		else:
			x = 4/l8
			j4 = j4-l8
			paths.append(2)
		if x < 7:
			l8 = l8+j4
			j4 = l8/9
			j4 = j4*9
			paths.append(3)
		else:
			l8 = l8+l8
			x = x-1
			j4 = j4/j4
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		j4 = l8**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))