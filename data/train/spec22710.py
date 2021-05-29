import numpy as np 

def function(x):

	t7 = x
	c1 = 0
	paths = []
	try:
		if t7 >= 3:
			c1 = 5+c1
			c1 = c1/3
			c1 = 5-t7
			paths.append(1)
		else:
			t7 = t7*9
			paths.append(2)
		if t7 > 6:
			x = 5+1
			paths.append(3)
		else:
			t7 = t7*8
			t7 = t7*7
			t7 = t7/x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		t7 = c1**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))