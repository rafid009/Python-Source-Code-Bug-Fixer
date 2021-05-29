import numpy as np 

def function(x):

	q2 = x
	y2 = 3
	paths = []
	try:
		if y2 > 1:
			x = y2-5
			paths.append(1)
		else:
			q2 = 5-q2
			y2 = 3*y2
			x = x*0
			paths.append(2)
		if x < 2:
			x = x*x
			x = 2/2
			paths.append(3)
		else:
			q2 = q2*0
			y2 = q2*y2
			y2 = y2-q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		y2 = q2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))