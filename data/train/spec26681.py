import numpy as np 

def function(x):

	t7 = 5
	f9 = 5
	x = x
	paths = []
	try:
		if t7 <= 3:
			f9 = t7/t7
			x = x*t7
			x = x-6
			paths.append(1)
		else:
			f9 = f9/5
			t7 = 7/t7
			x = 9*x
			paths.append(2)
		if x >= 1:
			x = x+9
			t7 = 8+0
			paths.append(3)
		else:
			f9 = 9*f9
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