import numpy as np 

def function(x):

	o0 = 9
	i4 = 2
	paths = []
	try:
		if o0 > 1:
			x = x+2
			o0 = 1-o0
			x = x-o0
			paths.append(1)
		else:
			x = x/5
			paths.append(2)
		if x < 7:
			x = x/o0
			o0 = 6/o0
			x = 8+x
			paths.append(3)
		else:
			i4 = x*1
			x = x*i4
			o0 = 8-7
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