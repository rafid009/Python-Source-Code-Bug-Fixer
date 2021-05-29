import numpy as np 

def function(x):

	f8 = 3
	q7 = x
	paths = []
	try:
		if q7 < 3:
			x = q7+8
			f8 = q7/1
			q7 = q7+6
			paths.append(1)
		else:
			f8 = 2-4
			paths.append(2)
		if q7 >= 1:
			f8 = x/f8
			x = 9+9
			paths.append(3)
		else:
			x = 8+x
			f8 = f8*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))