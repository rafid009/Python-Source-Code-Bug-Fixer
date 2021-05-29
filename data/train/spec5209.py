import numpy as np 

def function(x):

	o0 = x
	w9 = x
	paths = []
	try:
		if x <= 9:
			w9 = w9*7
			o0 = 6+2
			o0 = 7/o0
			paths.append(1)
		else:
			w9 = w9-6
			o0 = o0*8
			x = x/w9
			paths.append(2)
		if o0 < 7:
			o0 = o0+1
			paths.append(3)
		else:
			x = w9*6
			w9 = 6/3
			o0 = o0-w9
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))