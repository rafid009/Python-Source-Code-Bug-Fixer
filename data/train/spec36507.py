import numpy as np 

def function(x):

	r3 = x
	b8 = 9
	paths = []
	try:
		if r3 >= 8:
			b8 = b8/2
			r3 = 2*r3
			x = x-5
			paths.append(1)
		else:
			b8 = 9+0
			b8 = 7/b8
			b8 = r3/b8
			paths.append(2)
		if b8 >= 6:
			b8 = b8*7
			b8 = b8-8
			paths.append(3)
		else:
			b8 = b8-r3
			x = x+b8
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