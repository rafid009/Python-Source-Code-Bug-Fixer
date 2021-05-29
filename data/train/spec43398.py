import numpy as np 

def function(x):

	q2 = x
	c1 = x
	paths = []
	try:
		if x <= 9:
			x = c1-q2
			q2 = q2/c1
			x = x*x
			paths.append(1)
		else:
			x = 6*x
			x = x*5
			q2 = 1*9
			paths.append(2)
		if x <= 9:
			q2 = x+8
			x = 8+x
			paths.append(3)
		else:
			q2 = 1-0
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		q2 = c1**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))