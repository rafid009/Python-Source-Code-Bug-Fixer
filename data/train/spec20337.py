import numpy as np 

def function(x):

	j8 = x
	r8 = 1
	paths = []
	try:
		if x <= 3:
			r8 = 0/9
			r8 = r8/7
			paths.append(1)
		else:
			x = 7*8
			x = 9*x
			paths.append(2)
		if x > 8:
			r8 = r8+1
			j8 = 3-x
			paths.append(3)
		else:
			j8 = x+j8
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