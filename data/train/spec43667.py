import numpy as np 

def function(x):

	t6 = 9
	r7 = 6
	paths = []
	try:
		if r7 < 2:
			x = x/x
			x = x+1
			x = 2+x
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if r7 >= 3:
			x = 9-x
			paths.append(3)
		else:
			r7 = r7-6
			r7 = r7/1
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))