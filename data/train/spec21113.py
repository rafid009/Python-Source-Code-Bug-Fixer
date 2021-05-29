import numpy as np 

def function(x):

	t6 = x
	x1 = x
	paths = []
	try:
		if x1 <= 1:
			x = 1*x
			x1 = x-0
			paths.append(1)
		else:
			t6 = 9/t6
			x = 2+x
			paths.append(2)
		if t6 < 5:
			t6 = 3-t6
			paths.append(3)
		else:
			x1 = 6+0
			x1 = 0/5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))