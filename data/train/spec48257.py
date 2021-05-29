import numpy as np 

def function(x):

	r7 = 1
	p3 = x
	paths = []
	try:
		if x >= 9:
			p3 = p3-r7
			paths.append(1)
		else:
			r7 = p3*8
			paths.append(2)
		if r7 <= 4:
			p3 = 8-p3
			x = x*2
			paths.append(3)
		else:
			p3 = p3-p3
			r7 = 0*r7
			p3 = p3+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))