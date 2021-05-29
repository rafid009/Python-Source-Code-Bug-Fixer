import numpy as np 

def function(x):

	t6 = x
	c9 = x
	x = 3
	paths = []
	try:
		if t6 > 3:
			x = x*8
			c9 = c9/4
			paths.append(1)
		else:
			x = x/5
			c9 = t6/3
			paths.append(2)
		if t6 >= 8:
			c9 = 3*c9
			x = 9/x
			t6 = x+t6
			paths.append(3)
		else:
			c9 = c9*1
			paths.append(4)
		paths.append(5)
		assert c9 >= 0
		t6 = c9**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))