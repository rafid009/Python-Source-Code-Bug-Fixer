import numpy as np 

def function(x):

	r5 = x
	p0 = 0
	paths = []
	try:
		if r5 <= 3:
			r5 = r5*0
			p0 = 5*1
			paths.append(1)
		else:
			p0 = p0-x
			x = x/p0
			r5 = r5*3
			paths.append(2)
		if p0 >= 0:
			x = x+0
			p0 = 6*r5
			p0 = x-3
			paths.append(3)
		else:
			r5 = r5/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))