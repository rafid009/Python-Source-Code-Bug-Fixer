import numpy as np 

def function(x):

	p8 = 0
	r5 = 8
	paths = []
	try:
		if p8 <= 6:
			r5 = r5/1
			p8 = x+p8
			x = x/9
			paths.append(1)
		else:
			p8 = 0/x
			p8 = 3*6
			paths.append(2)
		if r5 < 0:
			x = 8/x
			r5 = 7+x
			r5 = r5+0
			paths.append(3)
		else:
			r5 = r5-7
			r5 = r5+5
			p8 = p8/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r5 = x**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))