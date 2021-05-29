import numpy as np 

def function(x):

	l5 = 1
	y3 = x
	x = 1
	paths = []
	try:
		if l5 <= 7:
			x = x/7
			paths.append(1)
		else:
			l5 = x-l5
			l5 = 4*1
			paths.append(2)
		if y3 > 4:
			x = 9+x
			l5 = 1*6
			x = 5*x
			paths.append(3)
		else:
			y3 = y3+3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))