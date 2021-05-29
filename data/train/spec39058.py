import numpy as np 

def function(x):

	r6 = x
	p2 = 8
	paths = []
	try:
		if p2 < 4:
			r6 = r6/7
			p2 = x-1
			paths.append(1)
		else:
			r6 = r6/x
			x = x*x
			paths.append(2)
		if x > 4:
			p2 = 3*p2
			x = 4+x
			p2 = 5-9
			paths.append(3)
		else:
			r6 = r6+r6
			p2 = 1-p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		r6 = p2**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))