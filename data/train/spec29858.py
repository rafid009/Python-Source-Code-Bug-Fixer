import numpy as np 

def function(x):

	q4 = x
	f5 = 3
	paths = []
	try:
		if q4 <= 4:
			f5 = 7/f5
			x = x*5
			q4 = q4/6
			paths.append(1)
		else:
			f5 = x-f5
			f5 = 7-f5
			paths.append(2)
		if q4 > 4:
			q4 = 9*q4
			q4 = q4-x
			paths.append(3)
		else:
			x = 3/x
			q4 = q4/5
			q4 = 0*q4
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))