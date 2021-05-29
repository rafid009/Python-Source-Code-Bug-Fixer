import numpy as np 

def function(x):

	i5 = x
	r7 = x
	x = x
	paths = []
	try:
		if r7 >= 6:
			i5 = 3/i5
			r7 = 2*r7
			paths.append(1)
		else:
			x = x+5
			i5 = i5*r7
			i5 = 2/i5
			paths.append(2)
		if i5 >= 6:
			i5 = r7*r7
			x = 3*2
			i5 = i5-x
			paths.append(3)
		else:
			r7 = i5/r7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r7 = x**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))