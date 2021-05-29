import numpy as np 

def function(x):

	p7 = x
	r6 = x
	paths = []
	try:
		if p7 < 1:
			p7 = 1+4
			paths.append(1)
		else:
			p7 = r6/5
			paths.append(2)
		if r6 <= 8:
			p7 = p7+3
			p7 = p7/x
			paths.append(3)
		else:
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		r6 = p7**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))