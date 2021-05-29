import numpy as np 

def function(x):

	i9 = 4
	t1 = 2
	paths = []
	try:
		if i9 >= 2:
			t1 = 4/4
			paths.append(1)
		else:
			i9 = 0/2
			paths.append(2)
		if x <= 9:
			i9 = i9-1
			i9 = 9/1
			paths.append(3)
		else:
			x = x*4
			t1 = x*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))