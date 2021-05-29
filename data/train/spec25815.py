import numpy as np 

def function(x):

	r2 = x
	c1 = x
	paths = []
	try:
		if x > 0:
			c1 = c1*c1
			r2 = 7*r2
			r2 = x+r2
			paths.append(1)
		else:
			x = x-7
			x = 9-x
			paths.append(2)
		if x <= 4:
			r2 = r2+7
			r2 = r2-c1
			paths.append(3)
		else:
			x = x/7
			x = 8/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))