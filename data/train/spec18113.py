import numpy as np 

def function(x):

	o0 = x
	l5 = x
	paths = []
	try:
		if l5 < 9:
			x = 0*8
			l5 = 6-l5
			x = x+8
			paths.append(1)
		else:
			o0 = o0+l5
			x = x-6
			paths.append(2)
		if l5 < 7:
			o0 = 3-4
			o0 = o0+0
			paths.append(3)
		else:
			l5 = 5*l5
			o0 = o0*o0
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))