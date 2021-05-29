import numpy as np 

def function(x):

	t3 = x
	x4 = x
	paths = []
	try:
		if x4 <= 2:
			x4 = 3/x4
			t3 = t3/7
			paths.append(1)
		else:
			x4 = 4+1
			x4 = 0-x4
			t3 = t3/t3
			paths.append(2)
		if x <= 5:
			t3 = t3/1
			x = x+5
			x = t3*x
			paths.append(3)
		else:
			t3 = 3-t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))