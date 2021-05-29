import numpy as np 

def function(x):

	w9 = x
	o0 = 7
	paths = []
	try:
		if x <= 8:
			x = x*9
			paths.append(1)
		else:
			o0 = 5/2
			x = x/9
			paths.append(2)
		if o0 <= 0:
			x = 7+2
			w9 = w9+5
			paths.append(3)
		else:
			w9 = 9/x
			x = x/7
			x = 5/5
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		o0 = w9**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))