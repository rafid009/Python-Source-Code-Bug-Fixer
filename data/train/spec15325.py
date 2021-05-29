import numpy as np 

def function(x):

	j4 = 2
	l9 = 6
	paths = []
	try:
		if l9 < 8:
			x = 5+x
			paths.append(1)
		else:
			x = 6-x
			x = 8+l9
			paths.append(2)
		if x < 5:
			j4 = 6+9
			paths.append(3)
		else:
			l9 = l9*8
			x = 1*6
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