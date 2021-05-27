import numpy as np 

def function(x):

	j0 = 9
	l6 = x
	x = x
	paths = []
	try:
		if x <= 5:
			j0 = 7/j0
			l6 = l6*1
			paths.append(1)
		else:
			j0 = 8-9
			j0 = j0-5
			paths.append(2)
		if l6 < 7:
			l6 = j0-0
			l6 = l6+0
			x = x/4
			paths.append(3)
		else:
			x = x-x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))