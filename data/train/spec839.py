import numpy as np 

def function(x):

	r5 = 1
	p1 = 0
	paths = []
	try:
		if r5 < 6:
			r5 = r5*x
			r5 = r5-r5
			paths.append(1)
		else:
			x = p1/p1
			x = x+r5
			paths.append(2)
		if x > 1:
			r5 = r5*1
			paths.append(3)
		else:
			p1 = x/8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))