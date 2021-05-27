import numpy as np 

def function(x):

	q7 = x
	b4 = x
	x = x
	paths = []
	try:
		if x <= 4:
			x = q7+x
			x = 9*1
			paths.append(1)
		else:
			x = x*b4
			paths.append(2)
		if x <= 0:
			b4 = q7-8
			b4 = 1-9
			x = x/q7
			paths.append(3)
		else:
			b4 = q7+q7
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		q7 = b4**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))