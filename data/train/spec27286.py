import numpy as np 

def function(x):

	q9 = 1
	y4 = 5
	x = x
	paths = []
	try:
		if x < 9:
			x = x*2
			paths.append(1)
		else:
			q9 = q9-5
			paths.append(2)
		if q9 < 5:
			y4 = y4/y4
			x = x/8
			paths.append(3)
		else:
			x = x/9
			x = 4+9
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