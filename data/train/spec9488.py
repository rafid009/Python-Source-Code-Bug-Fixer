import numpy as np 

def function(x):

	o0 = 6
	b4 = 9
	x = x
	paths = []
	try:
		if b4 >= 3:
			o0 = x+o0
			b4 = b4+6
			paths.append(1)
		else:
			x = 7*0
			b4 = 7/b4
			b4 = o0-2
			paths.append(2)
		if x < 9:
			b4 = b4*3
			b4 = b4+o0
			paths.append(3)
		else:
			o0 = 1*o0
			b4 = b4*b4
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