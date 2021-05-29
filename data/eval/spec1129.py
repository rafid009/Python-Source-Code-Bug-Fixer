import numpy as np 

def function(x):

	l9 = x
	v7 = 0
	paths = []
	try:
		if x < 5:
			v7 = x-v7
			l9 = l9/v7
			l9 = l9-6
			paths.append(1)
		else:
			v7 = 8-v7
			l9 = 1/l9
			paths.append(2)
		if v7 > 4:
			l9 = v7/3
			l9 = 8-3
			x = 1+9
			paths.append(3)
		else:
			l9 = 3-6
			v7 = v7+l9
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))