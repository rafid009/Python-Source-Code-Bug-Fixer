import numpy as np 

def function(x):

	q8 = x
	c7 = x
	x = x
	paths = []
	try:
		if q8 > 3:
			c7 = c7+1
			q8 = 0/1
			paths.append(1)
		else:
			c7 = 2-c7
			q8 = q8*5
			paths.append(2)
		if q8 < 5:
			x = x-0
			c7 = x*3
			paths.append(3)
		else:
			c7 = x+2
			q8 = c7+x
			q8 = q8-4
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))