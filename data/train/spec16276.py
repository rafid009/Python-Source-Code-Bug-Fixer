import numpy as np 

def function(x):

	y2 = 7
	l5 = 3
	paths = []
	try:
		if x >= 8:
			y2 = 0+y2
			l5 = 8+l5
			paths.append(1)
		else:
			l5 = y2/1
			y2 = y2+1
			y2 = y2+5
			paths.append(2)
		if l5 < 5:
			y2 = l5/5
			paths.append(3)
		else:
			l5 = 8+l5
			y2 = x*7
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		x = y2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))