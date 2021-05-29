import numpy as np 

def function(x):

	o0 = x
	w5 = x
	x = 1
	paths = []
	try:
		if x <= 9:
			x = 9/o0
			paths.append(1)
		else:
			o0 = o0*0
			x = x-2
			w5 = 4/6
			paths.append(2)
		if o0 > 5:
			o0 = o0-o0
			paths.append(3)
		else:
			w5 = w5*6
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