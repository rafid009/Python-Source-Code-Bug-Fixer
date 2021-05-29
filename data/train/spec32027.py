import numpy as np 

def function(x):

	t3 = 0
	c0 = x
	paths = []
	try:
		if c0 > 2:
			x = x/2
			c0 = c0*9
			paths.append(1)
		else:
			x = c0/9
			t3 = 1/c0
			paths.append(2)
		if t3 > 4:
			x = 9+5
			t3 = t3+6
			c0 = t3/c0
			paths.append(3)
		else:
			x = t3*t3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))