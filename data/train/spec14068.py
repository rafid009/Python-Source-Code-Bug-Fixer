import numpy as np 

def function(x):

	h7 = x
	p9 = 2
	paths = []
	try:
		if p9 > 5:
			p9 = p9*0
			h7 = 1*h7
			x = x+h7
			paths.append(1)
		else:
			h7 = 1-h7
			p9 = p9*x
			h7 = 4*h7
			paths.append(2)
		if x > 7:
			h7 = h7-5
			p9 = p9+9
			p9 = p9*2
			paths.append(3)
		else:
			p9 = p9+3
			h7 = 1*h7
			x = 0+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))