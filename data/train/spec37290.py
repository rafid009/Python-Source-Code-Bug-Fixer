import numpy as np 

def function(x):

	b8 = x
	r8 = x
	paths = []
	try:
		if x < 3:
			b8 = b8*x
			b8 = 2/b8
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x < 2:
			b8 = b8-5
			paths.append(3)
		else:
			r8 = 2*4
			r8 = 1/4
			x = 2/1
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))