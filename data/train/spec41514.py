import numpy as np 

def function(x):

	o0 = x
	p9 = 3
	paths = []
	try:
		if o0 > 4:
			p9 = 0+p9
			o0 = 7-o0
			p9 = 2*o0
			paths.append(1)
		else:
			x = 3-x
			o0 = o0*8
			p9 = p9+p9
			paths.append(2)
		if o0 <= 6:
			o0 = 8*7
			x = 3-x
			o0 = 1-o0
			paths.append(3)
		else:
			x = x*6
			x = x*4
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))