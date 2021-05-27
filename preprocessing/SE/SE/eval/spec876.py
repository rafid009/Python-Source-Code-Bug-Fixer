import numpy as np 

def function(x):

	t7 = 5
	r7 = x
	paths = []
	try:
		if x <= 3:
			t7 = 7-t7
			paths.append(1)
		else:
			x = x/6
			r7 = r7/t7
			x = x+5
			paths.append(2)
		if x >= 5:
			r7 = 4-r7
			x = x/6
			paths.append(3)
		else:
			r7 = 8/t7
			t7 = 6-t7
			t7 = t7*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))