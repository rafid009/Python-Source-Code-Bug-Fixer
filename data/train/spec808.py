import numpy as np 

def function(x):

	o0 = x
	p8 = 4
	paths = []
	try:
		if x >= 9:
			p8 = 4/p8
			x = x*p8
			p8 = p8*8
			paths.append(1)
		else:
			p8 = p8+3
			x = x+5
			x = o0-5
			paths.append(2)
		if x <= 6:
			p8 = p8-p8
			o0 = x*9
			p8 = x/1
			paths.append(3)
		else:
			x = 0+9
			o0 = 2/o0
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