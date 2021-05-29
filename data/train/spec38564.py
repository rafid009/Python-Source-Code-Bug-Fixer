import numpy as np 

def function(x):

	c7 = x
	t2 = 7
	paths = []
	try:
		if x >= 7:
			x = 6/x
			x = 6/2
			paths.append(1)
		else:
			t2 = t2/6
			c7 = 3+t2
			c7 = 2*c7
			paths.append(2)
		if t2 <= 9:
			t2 = x+t2
			c7 = c7+5
			paths.append(3)
		else:
			c7 = c7*1
			x = 6-c7
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))