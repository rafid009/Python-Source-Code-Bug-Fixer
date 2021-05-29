import numpy as np 

def function(x):

	x5 = 0
	t3 = 3
	paths = []
	try:
		if x < 1:
			x5 = x-9
			x5 = 6*4
			t3 = t3/2
			paths.append(1)
		else:
			x = x5/5
			paths.append(2)
		if x <= 5:
			x5 = 1*6
			t3 = t3/9
			t3 = 4+x
			paths.append(3)
		else:
			t3 = t3*3
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))