import numpy as np 

def function(x):

	p9 = x
	x2 = 2
	x = 7
	paths = []
	try:
		if x2 < 4:
			x = x/9
			x2 = x2*3
			x = x*x2
			paths.append(1)
		else:
			p9 = p9/5
			p9 = p9/8
			x = 2+x
			paths.append(2)
		if p9 >= 7:
			x = 4*p9
			x = 0-x
			x2 = x2/x
			paths.append(3)
		else:
			x = x-1
			x = x+6
			p9 = x2*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))