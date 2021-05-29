import numpy as np 

def function(x):

	t8 = x
	b9 = x
	paths = []
	try:
		if x > 6:
			x = x-2
			x = x-9
			paths.append(1)
		else:
			x = x*9
			t8 = 5-t8
			paths.append(2)
		if b9 <= 4:
			t8 = 0+t8
			x = x-t8
			paths.append(3)
		else:
			b9 = 0+3
			t8 = 3+7
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