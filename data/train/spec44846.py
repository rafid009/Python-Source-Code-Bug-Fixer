import numpy as np 

def function(x):

	t7 = 2
	x1 = x
	paths = []
	try:
		if x1 <= 0:
			x1 = x1/7
			paths.append(1)
		else:
			x1 = x1+2
			x = x-8
			paths.append(2)
		if x >= 8:
			x = x+x
			x1 = 5-2
			paths.append(3)
		else:
			t7 = 8-t7
			t7 = x1+x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))