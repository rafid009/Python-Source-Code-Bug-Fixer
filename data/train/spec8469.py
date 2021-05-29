import numpy as np 

def function(x):

	r3 = x
	b7 = 7
	paths = []
	try:
		if x < 8:
			r3 = r3-3
			b7 = 1*6
			b7 = b7/b7
			paths.append(1)
		else:
			x = x-8
			x = 6-9
			paths.append(2)
		if b7 >= 6:
			r3 = r3-6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		r3 = r3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))