import numpy as np 

def function(x):

	y1 = x
	f3 = x
	paths = []
	try:
		if x >= 9:
			f3 = 7*3
			paths.append(1)
		else:
			x = x/5
			x = x+1
			paths.append(2)
		if f3 <= 5:
			x = y1+f3
			paths.append(3)
		else:
			f3 = f3+3
			x = x+7
			y1 = 6+y1
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