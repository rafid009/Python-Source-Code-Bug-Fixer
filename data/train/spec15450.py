import numpy as np 

def function(x):

	l0 = x
	l9 = 4
	paths = []
	try:
		if l9 < 0:
			x = x-7
			l0 = l0+x
			paths.append(1)
		else:
			l9 = 0-l9
			l0 = l0+0
			paths.append(2)
		if x < 5:
			x = l0+x
			paths.append(3)
		else:
			l0 = l0-x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))