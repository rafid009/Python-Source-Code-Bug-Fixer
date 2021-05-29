import numpy as np 

def function(x):

	f3 = x
	t2 = x
	paths = []
	try:
		if x <= 8:
			x = f3-x
			t2 = 4*t2
			paths.append(1)
		else:
			x = x/t2
			x = t2/f3
			x = x*5
			paths.append(2)
		if x > 6:
			f3 = 4-1
			t2 = t2*t2
			t2 = t2-f3
			paths.append(3)
		else:
			x = x-7
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