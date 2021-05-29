import numpy as np 

def function(x):

	v8 = x
	r2 = 3
	x = x
	paths = []
	try:
		if x < 8:
			x = 0+x
			paths.append(1)
		else:
			x = 3-6
			r2 = 0*4
			paths.append(2)
		if r2 <= 4:
			x = 0+x
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))