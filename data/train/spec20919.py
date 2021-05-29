import numpy as np 

def function(x):

	b7 = 6
	t2 = 5
	paths = []
	try:
		if t2 < 0:
			b7 = b7/b7
			x = x+t2
			t2 = t2+x
			paths.append(1)
		else:
			b7 = b7/4
			paths.append(2)
		if t2 >= 1:
			t2 = 6/t2
			t2 = t2/4
			paths.append(3)
		else:
			x = 4-7
			x = 1*x
			t2 = t2/9
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