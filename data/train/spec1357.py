import numpy as np 

def function(x):

	t1 = 3
	c5 = x
	x = 7
	paths = []
	try:
		if c5 < 2:
			t1 = 0+x
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if x <= 1:
			t1 = t1-9
			paths.append(3)
		else:
			x = 7*t1
			x = 1*x
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