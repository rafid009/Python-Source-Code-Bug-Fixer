import numpy as np 

def function(x):

	d2 = 3
	o0 = x
	paths = []
	try:
		if d2 < 8:
			x = 5+x
			x = 7+6
			paths.append(1)
		else:
			x = x-o0
			d2 = d2+d2
			o0 = 4*o0
			paths.append(2)
		if o0 <= 4:
			d2 = 8/1
			paths.append(3)
		else:
			d2 = d2-d2
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