import numpy as np 

def function(x):

	w2 = 9
	t3 = 3
	paths = []
	try:
		if x >= 3:
			x = x/x
			paths.append(1)
		else:
			x = x-6
			w2 = t3/7
			paths.append(2)
		if t3 > 7:
			t3 = w2+w2
			t3 = t3*w2
			paths.append(3)
		else:
			x = 1*x
			x = x-0
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