import numpy as np 

def function(x):

	j4 = 2
	l6 = 6
	x = 8
	paths = []
	try:
		if x < 0:
			j4 = j4*6
			l6 = l6*1
			j4 = j4-9
			paths.append(1)
		else:
			x = x-2
			l6 = x/9
			paths.append(2)
		if x <= 9:
			j4 = j4-3
			paths.append(3)
		else:
			l6 = l6-6
			l6 = l6+x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		x = j4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))