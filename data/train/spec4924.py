import numpy as np 

def function(x):

	f6 = 5
	y3 = 3
	paths = []
	try:
		if y3 <= 3:
			x = 1+x
			f6 = f6/f6
			paths.append(1)
		else:
			x = 0-1
			x = 7+y3
			paths.append(2)
		if f6 < 6:
			x = x-5
			f6 = f6/7
			paths.append(3)
		else:
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))