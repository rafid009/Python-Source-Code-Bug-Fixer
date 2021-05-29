import numpy as np 

def function(x):

	l6 = x
	j6 = x
	paths = []
	try:
		if j6 > 1:
			l6 = l6*0
			paths.append(1)
		else:
			l6 = j6/l6
			paths.append(2)
		if l6 > 1:
			l6 = 9*l6
			j6 = x-j6
			x = 4/l6
			paths.append(3)
		else:
			j6 = 8-9
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