import numpy as np 

def function(x):

	y6 = x
	q9 = x
	paths = []
	try:
		if y6 < 6:
			y6 = y6-q9
			y6 = y6-y6
			y6 = y6+9
			paths.append(1)
		else:
			q9 = 7+y6
			q9 = x+q9
			paths.append(2)
		if y6 >= 8:
			q9 = q9+6
			x = q9/8
			q9 = x/9
			paths.append(3)
		else:
			x = 3+x
			q9 = x/y6
			q9 = y6/3
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