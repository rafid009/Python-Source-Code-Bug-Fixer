import numpy as np 

def function(x):

	r7 = 4
	b9 = 6
	paths = []
	try:
		if r7 >= 2:
			b9 = b9/7
			paths.append(1)
		else:
			x = x/1
			r7 = r7/3
			r7 = r7*3
			paths.append(2)
		if x < 9:
			x = x/r7
			x = x*3
			b9 = b9/b9
			paths.append(3)
		else:
			r7 = 9-r7
			b9 = b9/2
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