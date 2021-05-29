import numpy as np 

def function(x):

	f8 = 5
	t5 = x
	paths = []
	try:
		if x < 9:
			t5 = 3-t5
			t5 = f8/3
			f8 = f8*7
			paths.append(1)
		else:
			t5 = x-t5
			paths.append(2)
		if x < 4:
			x = f8-5
			f8 = 5+t5
			t5 = t5-4
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))