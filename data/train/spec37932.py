import numpy as np 

def function(x):

	t5 = 4
	c4 = 7
	paths = []
	try:
		if x <= 8:
			t5 = 3-1
			x = x*9
			paths.append(1)
		else:
			t5 = t5+9
			paths.append(2)
		if t5 <= 2:
			t5 = t5/4
			paths.append(3)
		else:
			t5 = x*7
			t5 = t5/3
			c4 = 5-c4
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		t5 = c4**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))