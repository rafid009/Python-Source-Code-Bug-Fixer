import numpy as np 

def function(x):

	m9 = 8
	o0 = x
	paths = []
	try:
		if o0 <= 0:
			x = x*9
			m9 = x-x
			m9 = x+5
			paths.append(1)
		else:
			o0 = o0-2
			x = x+1
			o0 = o0/4
			paths.append(2)
		if o0 <= 6:
			o0 = 6*o0
			x = x/6
			paths.append(3)
		else:
			o0 = 8*o0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))