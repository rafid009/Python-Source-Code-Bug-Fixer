import numpy as np 

def function(x):

	q2 = x
	x7 = 2
	x = 5
	paths = []
	try:
		if x7 < 7:
			q2 = x7-q2
			paths.append(1)
		else:
			x7 = 0/x7
			paths.append(2)
		if x <= 9:
			x = x*2
			x = 4*q2
			x7 = 1+x7
			paths.append(3)
		else:
			x = x/3
			x7 = x7+3
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x7 = q2**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))