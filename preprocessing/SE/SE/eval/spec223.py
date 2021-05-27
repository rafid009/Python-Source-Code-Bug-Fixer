import numpy as np 

def function(x):

	t4 = 1
	f0 = x
	paths = []
	try:
		if x > 3:
			x = 3-1
			paths.append(1)
		else:
			f0 = x/7
			t4 = t4+3
			t4 = 3+x
			paths.append(2)
		if f0 >= 9:
			x = 8*f0
			paths.append(3)
		else:
			f0 = f0-t4
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))