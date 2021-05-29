import numpy as np 

def function(x):

	t0 = x
	b0 = 3
	paths = []
	try:
		if b0 <= 7:
			t0 = 5+x
			b0 = 1*b0
			paths.append(1)
		else:
			t0 = 9-b0
			paths.append(2)
		if x >= 3:
			x = 6-5
			x = x*3
			x = x+x
			paths.append(3)
		else:
			x = x/5
			b0 = 5+b0
			b0 = 8/b0
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		x = t0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))