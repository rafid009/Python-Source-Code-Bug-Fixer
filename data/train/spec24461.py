import numpy as np 

def function(x):

	t1 = 5
	x5 = 9
	paths = []
	try:
		if t1 <= 8:
			t1 = 0-t1
			x = x+5
			x = 3+x
			paths.append(1)
		else:
			t1 = x-t1
			x5 = 0-x5
			t1 = t1-0
			paths.append(2)
		if t1 < 1:
			t1 = x+1
			paths.append(3)
		else:
			x = 0*x
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