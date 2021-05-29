import numpy as np 

def function(x):

	k7 = x
	t1 = 7
	paths = []
	try:
		if x < 6:
			k7 = 6*k7
			paths.append(1)
		else:
			t1 = 9*6
			t1 = x-t1
			x = 7+x
			paths.append(2)
		if t1 < 1:
			t1 = t1+k7
			k7 = x-0
			x = 8/x
			paths.append(3)
		else:
			x = t1-6
			t1 = t1+t1
			t1 = 4*6
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