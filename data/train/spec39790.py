import numpy as np 

def function(x):

	p3 = x
	o0 = x
	paths = []
	try:
		if o0 > 4:
			p3 = x-1
			p3 = 5/o0
			o0 = 1+1
			paths.append(1)
		else:
			p3 = p3+9
			o0 = o0*6
			paths.append(2)
		if o0 <= 2:
			x = 5*p3
			x = 4*x
			x = x-p3
			paths.append(3)
		else:
			p3 = o0-p3
			p3 = p3-2
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))