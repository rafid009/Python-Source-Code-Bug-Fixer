import numpy as np 

def function(x):

	y4 = x
	t1 = x
	paths = []
	try:
		if y4 <= 5:
			t1 = t1+4
			y4 = t1*2
			paths.append(1)
		else:
			t1 = 7/y4
			paths.append(2)
		if y4 < 5:
			t1 = t1+2
			paths.append(3)
		else:
			x = 3-t1
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