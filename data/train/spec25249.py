import numpy as np 

def function(x):

	r0 = x
	x6 = x
	paths = []
	try:
		if x6 < 2:
			x = x+6
			x = 4/x
			paths.append(1)
		else:
			r0 = 3/3
			x = r0*x
			x6 = x6+7
			paths.append(2)
		if r0 >= 9:
			r0 = r0+5
			x6 = 0+7
			r0 = 9/9
			paths.append(3)
		else:
			x6 = x6/4
			r0 = r0+x
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))