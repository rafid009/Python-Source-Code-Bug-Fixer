import numpy as np 

def function(x):

	b5 = 8
	r8 = x
	x = x
	paths = []
	try:
		if b5 >= 7:
			b5 = 3/5
			paths.append(1)
		else:
			x = 2-r8
			paths.append(2)
		if b5 >= 0:
			b5 = 5+8
			paths.append(3)
		else:
			x = r8/6
			r8 = 2/b5
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))