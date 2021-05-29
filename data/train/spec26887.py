import numpy as np 

def function(x):

	p0 = 2
	b0 = 1
	paths = []
	try:
		if x <= 1:
			p0 = p0*8
			x = x*0
			paths.append(1)
		else:
			b0 = x+x
			x = x+5
			paths.append(2)
		if x > 7:
			b0 = 2-3
			paths.append(3)
		else:
			p0 = p0-x
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))