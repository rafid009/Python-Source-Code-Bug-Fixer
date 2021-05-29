import numpy as np 

def function(x):

	t9 = 2
	d7 = x
	paths = []
	try:
		if x > 2:
			t9 = 6/2
			paths.append(1)
		else:
			t9 = d7*t9
			paths.append(2)
		if d7 <= 5:
			x = x+9
			paths.append(3)
		else:
			t9 = 3/t9
			d7 = 9-d7
			d7 = 5+0
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))