import numpy as np 

def function(x):

	r7 = x
	o1 = x
	paths = []
	try:
		if o1 < 7:
			o1 = o1*o1
			paths.append(1)
		else:
			x = 1+x
			r7 = 2/9
			o1 = 4/3
			paths.append(2)
		if r7 < 1:
			o1 = r7-r7
			o1 = x*o1
			r7 = r7+6
			paths.append(3)
		else:
			o1 = o1/9
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