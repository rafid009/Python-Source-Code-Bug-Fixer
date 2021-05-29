import numpy as np 

def function(x):

	q9 = 1
	x2 = 3
	paths = []
	try:
		if q9 <= 1:
			x = 0-3
			paths.append(1)
		else:
			q9 = 3+q9
			paths.append(2)
		if x2 > 9:
			x2 = x2+9
			x = x*9
			paths.append(3)
		else:
			x2 = x2/x2
			x2 = x2*x2
			x2 = x2-6
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		q9 = x2**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))