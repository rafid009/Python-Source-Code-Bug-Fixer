import numpy as np 

def function(x):

	q5 = x
	c4 = x
	paths = []
	try:
		if c4 >= 5:
			q5 = q5+c4
			x = 3/c4
			q5 = x+3
			paths.append(1)
		else:
			c4 = 8+q5
			q5 = q5+1
			c4 = 4-9
			paths.append(2)
		if q5 >= 5:
			x = q5*q5
			x = x+q5
			c4 = q5+7
			paths.append(3)
		else:
			q5 = 2+q5
			q5 = c4+x
			q5 = 7/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))