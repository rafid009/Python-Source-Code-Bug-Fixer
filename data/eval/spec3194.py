import numpy as np 

def function(x):

	r0 = x
	r8 = x
	paths = []
	try:
		if x <= 6:
			x = x/7
			paths.append(1)
		else:
			r0 = x/1
			paths.append(2)
		if r0 <= 6:
			r8 = x/r8
			r0 = r8-r0
			paths.append(3)
		else:
			r8 = 2-7
			x = x/6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))