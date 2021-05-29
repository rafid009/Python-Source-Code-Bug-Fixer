import numpy as np 

def function(x):

	n8 = x
	l6 = 9
	paths = []
	try:
		if l6 > 4:
			n8 = n8/1
			l6 = x-l6
			paths.append(1)
		else:
			n8 = 8-7
			l6 = l6*8
			l6 = 2/l6
			paths.append(2)
		if l6 >= 6:
			l6 = l6-1
			l6 = l6*4
			paths.append(3)
		else:
			l6 = l6/l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))