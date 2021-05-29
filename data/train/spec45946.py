import numpy as np 

def function(x):

	t1 = x
	v2 = x
	x = 5
	paths = []
	try:
		if t1 >= 0:
			v2 = v2-1
			v2 = 3/8
			v2 = v2-7
			paths.append(1)
		else:
			x = x-t1
			t1 = t1-0
			paths.append(2)
		if t1 <= 6:
			t1 = 3-9
			t1 = 2-t1
			x = 2/t1
			paths.append(3)
		else:
			v2 = v2-8
			v2 = 8*9
			t1 = 2-t1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))