import numpy as np 

def function(x):

	r3 = x
	t3 = x
	paths = []
	try:
		if t3 >= 9:
			t3 = 4*t3
			paths.append(1)
		else:
			x = x-3
			x = t3/8
			x = 5*x
			paths.append(2)
		if x < 2:
			x = x/6
			paths.append(3)
		else:
			t3 = 5*x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))