import numpy as np 

def function(x):

	r0 = x
	r8 = 3
	paths = []
	try:
		if x > 0:
			x = x/7
			r0 = r0*x
			x = x-5
			paths.append(1)
		else:
			x = 0+2
			r0 = r0-r0
			r8 = r8-6
			paths.append(2)
		if x <= 3:
			r8 = r8-7
			x = r0*r0
			r8 = r8/6
			paths.append(3)
		else:
			r8 = r8/2
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