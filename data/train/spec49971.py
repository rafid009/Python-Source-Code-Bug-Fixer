import numpy as np 

def function(x):

	p1 = x
	r2 = 2
	paths = []
	try:
		if p1 > 9:
			p1 = 1+p1
			paths.append(1)
		else:
			p1 = p1+5
			p1 = 2*x
			paths.append(2)
		if p1 >= 1:
			p1 = 7-p1
			paths.append(3)
		else:
			x = x*p1
			p1 = p1-p1
			r2 = r2-p1
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		r2 = p1**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))