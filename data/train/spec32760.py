import numpy as np 

def function(x):

	r6 = x
	v8 = 4
	paths = []
	try:
		if x <= 7:
			v8 = v8+4
			paths.append(1)
		else:
			x = x-v8
			x = x*r6
			r6 = x/r6
			paths.append(2)
		if x < 6:
			x = 2*x
			paths.append(3)
		else:
			v8 = 4/4
			r6 = r6/5
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))