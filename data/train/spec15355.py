import numpy as np 

def function(x):

	l2 = 1
	t6 = 0
	paths = []
	try:
		if t6 < 7:
			x = 8+0
			paths.append(1)
		else:
			x = x-t6
			l2 = 8*l2
			x = l2*x
			paths.append(2)
		if t6 < 7:
			t6 = t6-4
			paths.append(3)
		else:
			t6 = t6/6
			l2 = l2+7
			t6 = 2-8
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))