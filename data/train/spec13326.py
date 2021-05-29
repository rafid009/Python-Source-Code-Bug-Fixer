import numpy as np 

def function(x):

	t7 = 9
	f2 = 9
	paths = []
	try:
		if f2 >= 4:
			f2 = f2*6
			paths.append(1)
		else:
			x = 1/x
			x = 0-8
			paths.append(2)
		if x <= 6:
			t7 = t7-9
			x = 0-1
			f2 = 3/f2
			paths.append(3)
		else:
			f2 = 7*f2
			f2 = 7-6
			f2 = f2*9
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