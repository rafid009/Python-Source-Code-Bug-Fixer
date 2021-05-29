import numpy as np 

def function(x):

	t7 = 1
	c8 = 5
	paths = []
	try:
		if x <= 3:
			c8 = t7-x
			paths.append(1)
		else:
			c8 = c8/3
			paths.append(2)
		if t7 > 6:
			t7 = 2-t7
			x = x+x
			paths.append(3)
		else:
			x = x/t7
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		t7 = c8**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))