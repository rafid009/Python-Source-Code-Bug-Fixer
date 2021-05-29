import numpy as np 

def function(x):

	q8 = x
	o0 = x
	paths = []
	try:
		if o0 >= 0:
			x = x*x
			o0 = o0*1
			x = x-1
			paths.append(1)
		else:
			o0 = o0/7
			paths.append(2)
		if o0 <= 5:
			q8 = 6-q8
			x = 2*o0
			paths.append(3)
		else:
			o0 = o0/9
			q8 = o0/2
			o0 = x*o0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q8 = x**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))