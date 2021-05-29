import numpy as np 

def function(x):

	a1 = x
	r8 = 4
	paths = []
	try:
		if x > 4:
			x = 2/9
			paths.append(1)
		else:
			r8 = r8/5
			r8 = r8*2
			paths.append(2)
		if r8 >= 5:
			x = 9*r8
			r8 = 4-2
			x = 2*4
			paths.append(3)
		else:
			r8 = x*r8
			r8 = 7+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r8 = x**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))