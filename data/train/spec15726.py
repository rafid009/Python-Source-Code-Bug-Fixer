import numpy as np 

def function(x):

	t3 = 8
	y8 = x
	paths = []
	try:
		if x >= 5:
			t3 = t3-5
			paths.append(1)
		else:
			t3 = t3/x
			x = 0-8
			paths.append(2)
		if y8 < 1:
			x = x+x
			x = 3+t3
			paths.append(3)
		else:
			t3 = 1+y8
			t3 = x*6
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