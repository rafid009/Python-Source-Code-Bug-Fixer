import numpy as np 

def function(x):

	t1 = x
	c2 = x
	paths = []
	try:
		if x <= 4:
			c2 = 9*c2
			x = 4*c2
			c2 = c2+0
			paths.append(1)
		else:
			x = x+6
			x = x/8
			paths.append(2)
		if t1 >= 9:
			x = x*t1
			t1 = x/x
			c2 = c2/6
			paths.append(3)
		else:
			t1 = c2+t1
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		x = c2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))