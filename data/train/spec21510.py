import numpy as np 

def function(x):

	r3 = x
	b7 = 6
	paths = []
	try:
		if x > 8:
			x = 4/7
			paths.append(1)
		else:
			r3 = r3/8
			b7 = 8-9
			paths.append(2)
		if r3 < 9:
			r3 = r3/3
			r3 = 4/r3
			x = 1*9
			paths.append(3)
		else:
			x = x-x
			b7 = 0-b7
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