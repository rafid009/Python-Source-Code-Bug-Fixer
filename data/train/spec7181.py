import numpy as np 

def function(x):

	a8 = 5
	o0 = 7
	paths = []
	try:
		if o0 <= 6:
			o0 = o0+0
			x = a8+1
			o0 = o0/a8
			paths.append(1)
		else:
			o0 = 3+o0
			x = x*a8
			a8 = 0*a8
			paths.append(2)
		if o0 >= 7:
			a8 = 5-a8
			o0 = x-5
			paths.append(3)
		else:
			a8 = 6+a8
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))