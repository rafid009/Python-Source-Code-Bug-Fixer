import numpy as np 

def function(x):

	d9 = x
	o0 = 8
	x = x
	paths = []
	try:
		if d9 <= 3:
			o0 = o0*o0
			x = x/6
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if o0 < 8:
			x = 5/x
			d9 = 7+d9
			o0 = 5*o0
			paths.append(3)
		else:
			o0 = 3-o0
			o0 = o0-6
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		d9 = d9**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))