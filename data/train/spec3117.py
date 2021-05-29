import numpy as np 

def function(x):

	j0 = 8
	l5 = x
	paths = []
	try:
		if j0 >= 6:
			x = x*1
			j0 = 0+1
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x <= 4:
			x = x/j0
			x = 4+7
			paths.append(3)
		else:
			j0 = x*j0
			l5 = l5/l5
			j0 = 9*3
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))