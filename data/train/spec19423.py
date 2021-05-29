import numpy as np 

def function(x):

	r8 = 7
	b0 = x
	x = x
	paths = []
	try:
		if r8 <= 8:
			r8 = r8/6
			r8 = 3+r8
			paths.append(1)
		else:
			x = 6*7
			b0 = b0+7
			paths.append(2)
		if x <= 8:
			x = x+x
			r8 = b0*7
			paths.append(3)
		else:
			x = x/1
			x = x/2
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))