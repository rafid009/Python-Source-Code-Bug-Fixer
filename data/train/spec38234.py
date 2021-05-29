import numpy as np 

def function(x):

	y1 = x
	l9 = 9
	paths = []
	try:
		if x < 6:
			y1 = 7-5
			x = x-x
			l9 = l9/4
			paths.append(1)
		else:
			x = y1+6
			x = 3+x
			x = 5-x
			paths.append(2)
		if x <= 4:
			y1 = y1-3
			l9 = 7*6
			x = x*8
			paths.append(3)
		else:
			y1 = y1/x
			l9 = y1*5
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))