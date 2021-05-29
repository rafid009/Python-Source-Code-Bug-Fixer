import numpy as np 

def function(x):

	t1 = x
	u9 = 2
	paths = []
	try:
		if t1 >= 0:
			u9 = 2-8
			x = 8-x
			x = 2*2
			paths.append(1)
		else:
			x = u9+9
			paths.append(2)
		if x >= 0:
			t1 = 8/t1
			x = x-6
			x = 8/x
			paths.append(3)
		else:
			x = x+7
			t1 = 0-4
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