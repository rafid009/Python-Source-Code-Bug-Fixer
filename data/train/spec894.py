import numpy as np 

def function(x):

	f2 = 2
	q1 = x
	paths = []
	try:
		if x > 7:
			x = x/9
			paths.append(1)
		else:
			q1 = q1-9
			paths.append(2)
		if q1 > 1:
			f2 = f2+2
			paths.append(3)
		else:
			f2 = 4-4
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))