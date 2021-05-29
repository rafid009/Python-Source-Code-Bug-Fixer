import numpy as np 

def function(x):

	v8 = 2
	j6 = x
	paths = []
	try:
		if x < 3:
			v8 = 6-7
			v8 = 4+x
			x = x/8
			paths.append(1)
		else:
			j6 = 6-j6
			paths.append(2)
		if v8 > 1:
			x = x/j6
			x = x+x
			j6 = j6-7
			paths.append(3)
		else:
			v8 = v8+0
			x = x*4
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