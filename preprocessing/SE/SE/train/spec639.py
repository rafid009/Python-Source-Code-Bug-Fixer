import numpy as np 

def function(x):

	j5 = 8
	r4 = x
	paths = []
	try:
		if x < 9:
			j5 = 3/j5
			j5 = 8+j5
			x = r4-8
			paths.append(1)
		else:
			r4 = j5/9
			paths.append(2)
		if j5 <= 5:
			r4 = 6+x
			j5 = j5*9
			x = 1-4
			paths.append(3)
		else:
			x = 1-6
			r4 = r4*r4
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