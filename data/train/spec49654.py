import numpy as np 

def function(x):

	t3 = x
	c8 = x
	paths = []
	try:
		if x <= 5:
			t3 = 2*5
			t3 = t3+x
			paths.append(1)
		else:
			c8 = 1*t3
			paths.append(2)
		if t3 <= 4:
			x = x-4
			x = 9-x
			paths.append(3)
		else:
			t3 = t3-2
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))