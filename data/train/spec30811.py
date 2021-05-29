import numpy as np 

def function(x):

	t5 = x
	o3 = 3
	paths = []
	try:
		if x < 4:
			o3 = o3-9
			x = 5*x
			t5 = 3/2
			paths.append(1)
		else:
			x = 2-x
			x = 6/x
			paths.append(2)
		if x >= 3:
			o3 = x/o3
			paths.append(3)
		else:
			x = 9+x
			t5 = 3+3
			o3 = 6/t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))