import numpy as np 

def function(x):

	t1 = 6
	f3 = 4
	paths = []
	try:
		if f3 >= 4:
			t1 = t1-1
			f3 = 8-7
			x = x+6
			paths.append(1)
		else:
			t1 = 9-2
			f3 = 8-f3
			paths.append(2)
		if x >= 5:
			f3 = f3-7
			paths.append(3)
		else:
			x = x+2
			t1 = 9-0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))