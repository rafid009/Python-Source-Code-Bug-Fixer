import numpy as np 

def function(x):

	i4 = x
	p5 = 4
	paths = []
	try:
		if x <= 2:
			p5 = p5+5
			paths.append(1)
		else:
			p5 = p5/8
			i4 = i4*1
			paths.append(2)
		if i4 > 4:
			i4 = 3*i4
			i4 = 3/x
			paths.append(3)
		else:
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))