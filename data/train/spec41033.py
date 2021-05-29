import numpy as np 

def function(x):

	f7 = 0
	q2 = x
	paths = []
	try:
		if x > 7:
			x = 5+6
			q2 = q2*8
			paths.append(1)
		else:
			q2 = q2*f7
			x = x-8
			paths.append(2)
		if f7 <= 1:
			f7 = 3-f7
			f7 = q2/5
			q2 = q2+3
			paths.append(3)
		else:
			q2 = f7+q2
			q2 = 9/q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))