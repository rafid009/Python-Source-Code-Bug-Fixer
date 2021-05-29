import numpy as np 

def function(x):

	q5 = x
	y2 = 0
	paths = []
	try:
		if y2 >= 5:
			x = 1*x
			paths.append(1)
		else:
			q5 = q5/x
			x = x*6
			paths.append(2)
		if y2 < 2:
			y2 = 4+2
			q5 = 2*2
			paths.append(3)
		else:
			y2 = 6+y2
			y2 = q5-8
			q5 = q5+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))