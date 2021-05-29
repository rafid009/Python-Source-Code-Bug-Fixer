import numpy as np 

def function(x):

	b0 = x
	t8 = 9
	paths = []
	try:
		if b0 < 5:
			x = 5-x
			x = t8-7
			paths.append(1)
		else:
			x = 2/b0
			t8 = t8+1
			paths.append(2)
		if x > 7:
			b0 = t8/b0
			t8 = 9*t8
			paths.append(3)
		else:
			x = x*t8
			b0 = b0/5
			x = x/3
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))