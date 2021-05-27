import numpy as np 

def function(x):

	y7 = 1
	c5 = x
	paths = []
	try:
		if x <= 5:
			x = c5*3
			y7 = y7*c5
			paths.append(1)
		else:
			x = y7/1
			y7 = 7+y7
			paths.append(2)
		if c5 >= 3:
			x = 3*2
			y7 = 1*y7
			x = x/2
			paths.append(3)
		else:
			y7 = 4+x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		y7 = c5**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))