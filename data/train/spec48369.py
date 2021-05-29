import numpy as np 

def function(x):

	y6 = x
	q2 = x
	x = 0
	paths = []
	try:
		if q2 < 1:
			q2 = q2/5
			y6 = 8-x
			paths.append(1)
		else:
			q2 = y6+7
			y6 = 2+0
			y6 = y6*5
			paths.append(2)
		if y6 > 5:
			q2 = q2-y6
			paths.append(3)
		else:
			q2 = q2/6
			q2 = q2-4
			y6 = 7-y6
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		y6 = q2**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))