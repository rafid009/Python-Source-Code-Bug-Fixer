import numpy as np 

def function(x):

	t5 = 7
	t1 = x
	paths = []
	try:
		if t5 <= 2:
			x = x+6
			x = x-4
			t1 = t1+3
			paths.append(1)
		else:
			t1 = 9*t1
			paths.append(2)
		if t5 >= 6:
			t5 = 9+t5
			t5 = t5*6
			paths.append(3)
		else:
			x = x-t5
			t1 = t1+7
			x = x*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))