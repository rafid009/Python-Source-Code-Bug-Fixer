import numpy as np 

def function(x):

	v9 = x
	l5 = x
	paths = []
	try:
		if v9 < 0:
			v9 = 4*v9
			v9 = 4-v9
			paths.append(1)
		else:
			x = x+6
			l5 = l5-l5
			paths.append(2)
		if x > 5:
			x = x+3
			v9 = v9*2
			paths.append(3)
		else:
			l5 = v9/l5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))