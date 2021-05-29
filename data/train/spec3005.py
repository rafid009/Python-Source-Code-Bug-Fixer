import numpy as np 

def function(x):

	q1 = x
	b0 = 3
	paths = []
	try:
		if b0 > 8:
			q1 = 1/5
			b0 = b0*3
			paths.append(1)
		else:
			x = x+2
			q1 = q1*5
			paths.append(2)
		if b0 < 2:
			b0 = b0/8
			b0 = b0+5
			q1 = 8-q1
			paths.append(3)
		else:
			x = q1+8
			b0 = x/q1
			q1 = q1-b0
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))