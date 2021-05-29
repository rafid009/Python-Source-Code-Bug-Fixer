import numpy as np 

def function(x):

	p3 = 8
	o0 = 7
	paths = []
	try:
		if x > 2:
			p3 = p3/o0
			p3 = 0+5
			paths.append(1)
		else:
			x = x/o0
			x = x/2
			p3 = p3*6
			paths.append(2)
		if o0 > 5:
			o0 = o0*7
			o0 = 6*x
			p3 = 0/1
			paths.append(3)
		else:
			p3 = p3+4
			o0 = 0*1
			o0 = o0-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))