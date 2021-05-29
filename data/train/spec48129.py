import numpy as np 

def function(x):

	c5 = 5
	t1 = x
	paths = []
	try:
		if x < 9:
			t1 = x-t1
			c5 = 7-3
			paths.append(1)
		else:
			x = x/x
			paths.append(2)
		if t1 > 8:
			x = 2+x
			x = 4+7
			x = t1+t1
			paths.append(3)
		else:
			c5 = x/c5
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		t1 = c5**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))