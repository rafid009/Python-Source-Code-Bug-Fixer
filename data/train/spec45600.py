import numpy as np 

def function(x):

	q9 = 0
	r1 = x
	paths = []
	try:
		if q9 >= 0:
			q9 = q9-6
			paths.append(1)
		else:
			r1 = q9/x
			x = x-r1
			paths.append(2)
		if r1 >= 0:
			q9 = 3-r1
			x = 4*7
			paths.append(3)
		else:
			x = 7+x
			r1 = r1+9
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