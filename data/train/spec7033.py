import numpy as np 

def function(x):

	t8 = 4
	c1 = x
	paths = []
	try:
		if x < 4:
			c1 = 7*c1
			x = 0-x
			paths.append(1)
		else:
			x = 7+8
			t8 = x*4
			t8 = x+t8
			paths.append(2)
		if t8 < 0:
			x = 2*0
			c1 = 5-c1
			paths.append(3)
		else:
			t8 = x-t8
			t8 = t8/8
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		t8 = c1**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))