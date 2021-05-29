import numpy as np 

def function(x):

	q9 = x
	y2 = 9
	paths = []
	try:
		if q9 > 4:
			q9 = y2-6
			paths.append(1)
		else:
			x = x+3
			paths.append(2)
		if y2 >= 0:
			y2 = y2+q9
			paths.append(3)
		else:
			q9 = x+q9
			q9 = q9*1
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))