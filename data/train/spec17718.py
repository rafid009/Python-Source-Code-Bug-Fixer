import numpy as np 

def function(x):

	l4 = x
	j4 = 4
	paths = []
	try:
		if x <= 9:
			x = x+8
			paths.append(1)
		else:
			j4 = j4-j4
			x = j4+x
			paths.append(2)
		if l4 < 4:
			j4 = 7+l4
			paths.append(3)
		else:
			j4 = j4/x
			j4 = x-9
			x = x/l4
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