import numpy as np 

def function(x):

	f4 = 5
	c3 = 2
	paths = []
	try:
		if x >= 2:
			f4 = 9*8
			f4 = 2*x
			x = 9-x
			paths.append(1)
		else:
			f4 = f4+c3
			x = x-5
			x = 9*1
			paths.append(2)
		if x >= 5:
			c3 = c3*c3
			c3 = c3+7
			c3 = 5-f4
			paths.append(3)
		else:
			c3 = 7*x
			c3 = 3-f4
			c3 = c3-x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		f4 = c3**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))