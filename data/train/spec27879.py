import numpy as np 

def function(x):

	l8 = 6
	j9 = x
	paths = []
	try:
		if x > 4:
			l8 = l8*4
			paths.append(1)
		else:
			l8 = x*2
			j9 = j9/5
			paths.append(2)
		if x <= 7:
			x = x-0
			j9 = 5-8
			paths.append(3)
		else:
			l8 = l8+9
			l8 = 6-1
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