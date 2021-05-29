import numpy as np 

def function(x):

	t1 = x
	v7 = 4
	x = 1
	paths = []
	try:
		if t1 >= 4:
			v7 = v7/9
			paths.append(1)
		else:
			x = x-7
			v7 = 2-v7
			t1 = t1/t1
			paths.append(2)
		if t1 > 3:
			t1 = t1-v7
			x = 4*x
			v7 = v7/3
			paths.append(3)
		else:
			x = x/3
			t1 = t1-v7
			t1 = t1-5
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