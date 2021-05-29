import numpy as np 

def function(x):

	t9 = 2
	x9 = 5
	paths = []
	try:
		if t9 >= 8:
			t9 = t9+0
			t9 = t9/9
			paths.append(1)
		else:
			t9 = 1-9
			t9 = t9-8
			x = x-1
			paths.append(2)
		if x < 6:
			x = 2-x
			paths.append(3)
		else:
			x9 = 4*0
			x = 4+x
			x9 = 3+x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))