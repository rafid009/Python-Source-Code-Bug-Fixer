import numpy as np 

def function(x):

	y1 = 9
	l5 = x
	paths = []
	try:
		if l5 < 5:
			x = 2+1
			l5 = 8*l5
			paths.append(1)
		else:
			l5 = 6*y1
			l5 = 8/l5
			y1 = 4/3
			paths.append(2)
		if y1 <= 0:
			y1 = 6*y1
			l5 = l5/9
			x = 0+7
			paths.append(3)
		else:
			x = y1*l5
			y1 = 1/7
			x = x/5
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