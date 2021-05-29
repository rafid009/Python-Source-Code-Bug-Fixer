import numpy as np 

def function(x):

	b0 = x
	p2 = 2
	paths = []
	try:
		if p2 > 0:
			p2 = p2-p2
			p2 = p2+x
			paths.append(1)
		else:
			p2 = b0*5
			b0 = x-7
			x = x-1
			paths.append(2)
		if b0 < 0:
			b0 = x+b0
			b0 = p2+b0
			paths.append(3)
		else:
			x = 4/x
			p2 = p2*1
			x = 5+8
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