import numpy as np 

def function(x):

	l8 = x
	j5 = x
	paths = []
	try:
		if x < 4:
			j5 = l8*x
			l8 = 7-l8
			l8 = j5*j5
			paths.append(1)
		else:
			l8 = l8+7
			j5 = j5/3
			x = x-5
			paths.append(2)
		if j5 <= 9:
			l8 = l8+8
			j5 = 7-j5
			paths.append(3)
		else:
			l8 = l8-2
			x = 9/x
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		x = j5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))