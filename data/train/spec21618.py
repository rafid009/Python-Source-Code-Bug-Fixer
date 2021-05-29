import numpy as np 

def function(x):

	o7 = x
	r7 = x
	paths = []
	try:
		if r7 < 5:
			o7 = 7+r7
			o7 = o7+x
			paths.append(1)
		else:
			x = x*o7
			r7 = r7/1
			paths.append(2)
		if o7 >= 3:
			o7 = 5-o7
			r7 = 1+r7
			paths.append(3)
		else:
			o7 = r7+4
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