import numpy as np 

def function(x):

	c9 = x
	y3 = 0
	paths = []
	try:
		if x <= 4:
			y3 = x+4
			y3 = 2+y3
			y3 = y3*x
			paths.append(1)
		else:
			c9 = y3/4
			x = x+9
			x = x+c9
			paths.append(2)
		if x > 2:
			y3 = 1+2
			y3 = 0+5
			paths.append(3)
		else:
			c9 = 3/c9
			y3 = y3*4
			c9 = 5/c9
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		x = c9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))