import numpy as np 

def function(x):

	l6 = x
	t5 = 8
	paths = []
	try:
		if l6 <= 6:
			l6 = l6*4
			x = 8/l6
			x = 7-x
			paths.append(1)
		else:
			l6 = 3*9
			paths.append(2)
		if t5 > 6:
			x = 4-6
			l6 = l6+0
			paths.append(3)
		else:
			x = x-0
			l6 = l6+l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))