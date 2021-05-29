import numpy as np 

def function(x):

	b8 = 8
	q7 = x
	paths = []
	try:
		if q7 < 2:
			b8 = b8-3
			x = 3*x
			x = x+4
			paths.append(1)
		else:
			x = q7*5
			b8 = 4/4
			x = q7+4
			paths.append(2)
		if b8 >= 0:
			q7 = q7-8
			x = x+x
			b8 = 8/5
			paths.append(3)
		else:
			x = 4+x
			b8 = 9/9
			b8 = b8+x
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))