import numpy as np 

def function(x):

	q5 = x
	q8 = 2
	paths = []
	try:
		if q5 <= 7:
			x = 2/1
			paths.append(1)
		else:
			q8 = q8*3
			q8 = q8/2
			q5 = x+2
			paths.append(2)
		if x < 3:
			q8 = q8-q5
			x = 6*2
			paths.append(3)
		else:
			x = 9*q5
			x = x+9
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))