import numpy as np 

def function(x):

	q2 = 2
	f8 = x
	paths = []
	try:
		if q2 > 6:
			x = x+9
			q2 = f8-f8
			paths.append(1)
		else:
			q2 = x+0
			paths.append(2)
		if f8 <= 9:
			q2 = 9*q2
			q2 = f8-q2
			paths.append(3)
		else:
			x = 8/x
			q2 = q2+4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))