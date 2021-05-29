import numpy as np 

def function(x):

	c4 = 4
	t7 = 1
	paths = []
	try:
		if x >= 4:
			c4 = 4+1
			c4 = c4+9
			x = t7*c4
			paths.append(1)
		else:
			c4 = t7-9
			paths.append(2)
		if t7 < 8:
			t7 = t7*5
			t7 = x/x
			paths.append(3)
		else:
			x = x-t7
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		t7 = c4**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))