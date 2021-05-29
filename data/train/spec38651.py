import numpy as np 

def function(x):

	p7 = x
	d1 = x
	paths = []
	try:
		if x <= 7:
			p7 = 3*2
			x = d1*p7
			p7 = p7/8
			paths.append(1)
		else:
			x = x*x
			p7 = 8-d1
			d1 = d1-8
			paths.append(2)
		if d1 >= 7:
			x = 3+x
			paths.append(3)
		else:
			p7 = d1+2
			d1 = x*d1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))