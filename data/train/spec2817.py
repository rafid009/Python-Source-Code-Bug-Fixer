import numpy as np 

def function(x):

	p6 = 4
	k6 = 8
	paths = []
	try:
		if x < 7:
			p6 = 4*4
			paths.append(1)
		else:
			k6 = x*k6
			x = p6-3
			k6 = 8+5
			paths.append(2)
		if p6 > 7:
			p6 = k6*x
			p6 = x+x
			x = x+1
			paths.append(3)
		else:
			k6 = k6/k6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p6 = x**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))