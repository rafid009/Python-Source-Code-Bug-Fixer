import numpy as np 

def function(x):

	h1 = 2
	t7 = 1
	paths = []
	try:
		if x >= 8:
			h1 = t7+h1
			h1 = h1-6
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if h1 > 1:
			x = 7+x
			x = 1*h1
			paths.append(3)
		else:
			t7 = t7/8
			t7 = t7+h1
			t7 = 8-t7
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		t7 = h1**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))