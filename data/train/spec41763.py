import numpy as np 

def function(x):

	q9 = 7
	r8 = 3
	paths = []
	try:
		if x < 8:
			r8 = q9*r8
			q9 = q9+r8
			x = x+9
			paths.append(1)
		else:
			x = x-r8
			r8 = r8*6
			paths.append(2)
		if r8 > 3:
			x = 2/x
			paths.append(3)
		else:
			q9 = 5*q9
			r8 = r8+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))