import numpy as np 

def function(x):

	c5 = 4
	t1 = 5
	paths = []
	try:
		if t1 < 4:
			c5 = c5+8
			paths.append(1)
		else:
			c5 = 5+0
			t1 = x/t1
			t1 = 4-x
			paths.append(2)
		if x < 3:
			t1 = t1+c5
			t1 = 4+t1
			paths.append(3)
		else:
			t1 = t1+8
			x = 6-x
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))