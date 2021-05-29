import numpy as np 

def function(x):

	t1 = 6
	x7 = x
	paths = []
	try:
		if x7 <= 9:
			t1 = 3-7
			x7 = t1/9
			paths.append(1)
		else:
			x = x/t1
			t1 = 6+x
			paths.append(2)
		if x7 >= 5:
			x = x-x
			t1 = x7-t1
			x7 = x7+t1
			paths.append(3)
		else:
			t1 = 5-x7
			x = x7/x7
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))