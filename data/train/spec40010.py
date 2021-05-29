import numpy as np 

def function(x):

	b8 = x
	t2 = x
	x = x
	paths = []
	try:
		if t2 < 2:
			x = x*5
			b8 = t2*b8
			x = x/3
			paths.append(1)
		else:
			t2 = 6/x
			paths.append(2)
		if x > 1:
			t2 = 1*b8
			paths.append(3)
		else:
			t2 = x/8
			x = x-0
			t2 = t2-3
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))