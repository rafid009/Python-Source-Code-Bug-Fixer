import numpy as np 

def function(x):

	p2 = x
	o0 = x
	x = x
	paths = []
	try:
		if o0 > 6:
			x = o0*x
			p2 = o0/p2
			o0 = 7*o0
			paths.append(1)
		else:
			o0 = o0*x
			paths.append(2)
		if o0 > 9:
			o0 = 3-4
			o0 = o0*1
			x = 1*x
			paths.append(3)
		else:
			o0 = x/9
			x = x/o0
			o0 = 8+8
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))