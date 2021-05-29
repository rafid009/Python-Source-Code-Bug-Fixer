import numpy as np 

def function(x):

	c5 = x
	p3 = x
	paths = []
	try:
		if x < 3:
			x = x+9
			x = 7*x
			x = 0/p3
			paths.append(1)
		else:
			x = x*2
			p3 = p3-4
			paths.append(2)
		if x >= 4:
			x = x/x
			c5 = c5-2
			paths.append(3)
		else:
			x = x-5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		x = c5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))