import numpy as np 

def function(x):

	l9 = 8
	o0 = x
	paths = []
	try:
		if x >= 7:
			x = 9-o0
			o0 = o0+7
			paths.append(1)
		else:
			o0 = 2-5
			l9 = 5/x
			paths.append(2)
		if x >= 1:
			o0 = o0*4
			o0 = 9-7
			o0 = 5*o0
			paths.append(3)
		else:
			x = x*6
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		o0 = l9**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))