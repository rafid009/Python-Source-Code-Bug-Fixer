import numpy as np 

def function(x):

	x2 = x
	t5 = x
	x = x
	paths = []
	try:
		if t5 < 3:
			t5 = t5*x
			x = 4*x
			paths.append(1)
		else:
			x = x+x2
			x = t5*x
			paths.append(2)
		if x >= 5:
			t5 = t5/1
			paths.append(3)
		else:
			x2 = 8+x2
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))