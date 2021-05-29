import numpy as np 

def function(x):

	x6 = 0
	l9 = x
	x = x
	paths = []
	try:
		if l9 <= 2:
			x6 = 4+x6
			x6 = x6+x
			l9 = l9-0
			paths.append(1)
		else:
			x6 = 9-x6
			paths.append(2)
		if l9 < 5:
			x = x+5
			l9 = 3+3
			paths.append(3)
		else:
			x6 = 8/9
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