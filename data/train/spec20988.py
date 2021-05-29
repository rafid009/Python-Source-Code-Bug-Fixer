import numpy as np 

def function(x):

	p5 = 6
	h0 = 4
	paths = []
	try:
		if h0 <= 7:
			h0 = h0+x
			p5 = 1-4
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if p5 >= 6:
			p5 = p5+h0
			p5 = h0/x
			p5 = 2-p5
			paths.append(3)
		else:
			h0 = 0*h0
			x = 8/x
			h0 = 0+h0
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))