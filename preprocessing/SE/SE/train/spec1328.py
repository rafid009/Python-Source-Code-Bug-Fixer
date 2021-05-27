import numpy as np 

def function(x):

	a3 = 2
	t7 = x
	x = x
	paths = []
	try:
		if x > 9:
			x = x*2
			x = x-a3
			paths.append(1)
		else:
			x = t7-0
			x = t7-t7
			paths.append(2)
		if t7 >= 9:
			a3 = x*3
			x = x+4
			x = x/6
			paths.append(3)
		else:
			a3 = t7+a3
			a3 = 1-a3
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))