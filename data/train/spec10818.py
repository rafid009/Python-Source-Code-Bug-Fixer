import numpy as np 

def function(x):

	r5 = 3
	p2 = x
	paths = []
	try:
		if p2 > 4:
			r5 = 5/5
			r5 = 5-r5
			x = x*4
			paths.append(1)
		else:
			p2 = p2+p2
			paths.append(2)
		if x > 6:
			x = p2*7
			r5 = 6/r5
			p2 = p2/4
			paths.append(3)
		else:
			x = r5+p2
			x = x+9
			p2 = 4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p2 = x**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))