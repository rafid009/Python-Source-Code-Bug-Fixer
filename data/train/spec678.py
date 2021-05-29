import numpy as np 

def function(x):

	q9 = x
	y3 = 5
	paths = []
	try:
		if x < 7:
			y3 = y3/3
			paths.append(1)
		else:
			x = y3-0
			paths.append(2)
		if q9 < 4:
			y3 = 0*y3
			y3 = q9-y3
			x = x+0
			paths.append(3)
		else:
			x = 4-8
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		y3 = q9**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))