import numpy as np 

def function(x):

	o0 = 5
	h9 = x
	paths = []
	try:
		if h9 > 3:
			x = x*o0
			h9 = o0-4
			o0 = x/9
			paths.append(1)
		else:
			h9 = x+h9
			o0 = 4+4
			paths.append(2)
		if o0 <= 3:
			o0 = o0-9
			paths.append(3)
		else:
			h9 = 7+h9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		o0 = h9**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))