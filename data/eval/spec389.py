import numpy as np 

def function(x):

	l5 = 9
	k7 = 8
	paths = []
	try:
		if x <= 1:
			l5 = x-k7
			x = x-2
			x = k7/l5
			paths.append(1)
		else:
			k7 = k7+4
			paths.append(2)
		if l5 > 4:
			k7 = 8-k7
			k7 = 0+4
			x = x/1
			paths.append(3)
		else:
			l5 = 1-l5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))