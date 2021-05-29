import numpy as np 

def function(x):

	q9 = x
	a8 = 9
	paths = []
	try:
		if q9 <= 6:
			q9 = q9+8
			q9 = 0*5
			q9 = 7*1
			paths.append(1)
		else:
			x = 9/x
			x = a8*0
			a8 = 5-1
			paths.append(2)
		if q9 > 5:
			a8 = a8*3
			q9 = 6+q9
			paths.append(3)
		else:
			a8 = a8*6
			x = x*a8
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