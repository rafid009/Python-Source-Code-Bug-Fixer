import numpy as np 

def function(x):

	t1 = 4
	f0 = x
	paths = []
	try:
		if x >= 7:
			t1 = t1-1
			paths.append(1)
		else:
			t1 = t1/f0
			t1 = 7/3
			x = x/3
			paths.append(2)
		if t1 <= 5:
			x = 5*7
			paths.append(3)
		else:
			t1 = t1+2
			t1 = 1+0
			x = f0/x
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