import numpy as np 

def function(x):

	p2 = 6
	y1 = x
	paths = []
	try:
		if y1 <= 2:
			p2 = 1-p2
			paths.append(1)
		else:
			p2 = p2*4
			x = x*x
			y1 = y1*p2
			paths.append(2)
		if y1 <= 9:
			y1 = p2+8
			x = 4+x
			paths.append(3)
		else:
			y1 = y1+1
			p2 = 7*p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))