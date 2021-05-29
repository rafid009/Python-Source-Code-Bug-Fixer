import numpy as np 

def function(x):

	x0 = x
	t7 = x
	paths = []
	try:
		if t7 <= 1:
			x = x-8
			t7 = t7/7
			x = 2/5
			paths.append(1)
		else:
			t7 = x-x0
			x0 = 5-6
			paths.append(2)
		if t7 < 7:
			t7 = x0+t7
			x = 1-8
			paths.append(3)
		else:
			x = x/1
			t7 = t7/t7
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		t7 = x0**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))