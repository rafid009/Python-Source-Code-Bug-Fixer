import numpy as np 

def function(x):

	b0 = 8
	q1 = x
	paths = []
	try:
		if b0 <= 3:
			x = x+x
			b0 = q1/3
			paths.append(1)
		else:
			b0 = b0*5
			q1 = 6-b0
			paths.append(2)
		if q1 > 3:
			q1 = q1-q1
			b0 = b0-9
			paths.append(3)
		else:
			x = 7+2
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		b0 = q1**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))