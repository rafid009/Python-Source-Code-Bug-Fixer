import numpy as np 

def function(x):

	p7 = 6
	k7 = x
	paths = []
	try:
		if k7 <= 4:
			p7 = p7-8
			p7 = p7/x
			x = p7*2
			paths.append(1)
		else:
			x = x-5
			x = 8/x
			k7 = k7+2
			paths.append(2)
		if p7 <= 6:
			x = x*p7
			x = x-9
			paths.append(3)
		else:
			k7 = 2*4
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		p7 = k7**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))