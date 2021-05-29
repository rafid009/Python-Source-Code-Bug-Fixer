import numpy as np 

def function(x):

	t1 = 2
	b7 = x
	paths = []
	try:
		if t1 >= 9:
			x = x*8
			t1 = t1/2
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if b7 <= 2:
			t1 = t1/t1
			b7 = 8*x
			paths.append(3)
		else:
			x = x*9
			x = x-2
			x = x*b7
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