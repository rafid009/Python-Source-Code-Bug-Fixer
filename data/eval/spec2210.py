import numpy as np 

def function(x):

	r9 = 7
	q2 = 2
	paths = []
	try:
		if x > 2:
			q2 = 0-4
			paths.append(1)
		else:
			x = 5+q2
			paths.append(2)
		if q2 >= 8:
			q2 = 5-4
			q2 = q2+1
			q2 = q2*8
			paths.append(3)
		else:
			q2 = q2-2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))