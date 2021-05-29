import numpy as np 

def function(x):

	c5 = x
	t4 = x
	paths = []
	try:
		if x < 2:
			x = x+1
			x = x*t4
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if c5 < 5:
			c5 = x/4
			paths.append(3)
		else:
			t4 = 2-t4
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))