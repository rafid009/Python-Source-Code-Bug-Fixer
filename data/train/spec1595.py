import numpy as np 

def function(x):

	t2 = 2
	c8 = 3
	paths = []
	try:
		if c8 < 6:
			x = 8*x
			x = x-5
			paths.append(1)
		else:
			x = x/t2
			t2 = c8-9
			c8 = c8+t2
			paths.append(2)
		if t2 <= 7:
			c8 = x-0
			x = c8+x
			paths.append(3)
		else:
			x = x-x
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		t2 = c8**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))