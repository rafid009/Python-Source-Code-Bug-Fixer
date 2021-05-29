import numpy as np 

def function(x):

	q9 = 0
	b9 = 8
	paths = []
	try:
		if q9 < 4:
			q9 = q9*0
			q9 = 8+6
			q9 = b9+3
			paths.append(1)
		else:
			b9 = b9-1
			paths.append(2)
		if q9 <= 4:
			q9 = 4+2
			b9 = 6*1
			paths.append(3)
		else:
			q9 = q9*9
			b9 = b9*q9
			q9 = q9*b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))