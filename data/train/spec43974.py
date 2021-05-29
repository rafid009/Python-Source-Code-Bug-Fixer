import numpy as np 

def function(x):

	p8 = x
	j4 = 4
	paths = []
	try:
		if x >= 3:
			x = 5*x
			p8 = x*9
			p8 = j4*p8
			paths.append(1)
		else:
			j4 = 2+j4
			p8 = p8/6
			paths.append(2)
		if p8 < 1:
			j4 = j4/4
			x = x+9
			paths.append(3)
		else:
			p8 = p8+j4
			p8 = x+p8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p8 = x**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))