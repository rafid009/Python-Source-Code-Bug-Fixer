import numpy as np 

def function(x):

	f6 = 9
	c5 = 4
	paths = []
	try:
		if f6 <= 3:
			x = x-7
			paths.append(1)
		else:
			c5 = c5-c5
			x = x+f6
			paths.append(2)
		if x < 9:
			f6 = f6/2
			x = f6/6
			f6 = 3-8
			paths.append(3)
		else:
			c5 = 0-c5
			f6 = x*c5
			x = x/5
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))