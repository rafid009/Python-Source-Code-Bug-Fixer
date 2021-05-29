import numpy as np 

def function(x):

	q5 = x
	y4 = 4
	x = 7
	paths = []
	try:
		if q5 > 3:
			y4 = y4*y4
			q5 = x-8
			x = x/x
			paths.append(1)
		else:
			y4 = y4-8
			y4 = y4*2
			paths.append(2)
		if y4 <= 2:
			q5 = 2-y4
			y4 = 7/y4
			paths.append(3)
		else:
			x = x-q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))