import numpy as np 

def function(x):

	k6 = x
	p2 = 1
	paths = []
	try:
		if p2 < 8:
			x = x-7
			p2 = p2*k6
			p2 = 4*p2
			paths.append(1)
		else:
			p2 = 9/p2
			p2 = p2-x
			paths.append(2)
		if x <= 2:
			p2 = p2/9
			paths.append(3)
		else:
			p2 = k6-p2
			k6 = k6+1
			p2 = p2*p2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))