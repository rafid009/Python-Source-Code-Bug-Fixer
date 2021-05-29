import numpy as np 

def function(x):

	p0 = x
	b3 = x
	x = 9
	paths = []
	try:
		if b3 < 6:
			b3 = b3/2
			p0 = p0*8
			paths.append(1)
		else:
			p0 = p0-5
			b3 = b3-b3
			paths.append(2)
		if x <= 8:
			x = x*7
			x = x/1
			p0 = b3*p0
			paths.append(3)
		else:
			b3 = b3/4
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))