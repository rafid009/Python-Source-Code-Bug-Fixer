import numpy as np 

def function(x):

	b3 = x
	q1 = x
	paths = []
	try:
		if q1 > 3:
			q1 = q1*b3
			paths.append(1)
		else:
			x = q1*6
			paths.append(2)
		if q1 >= 1:
			q1 = q1*2
			b3 = b3*2
			q1 = 1-0
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		b3 = q1**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))