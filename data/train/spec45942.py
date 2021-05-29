import numpy as np 

def function(x):

	p9 = x
	v7 = 5
	paths = []
	try:
		if p9 >= 8:
			x = x-1
			p9 = x-p9
			p9 = 1/x
			paths.append(1)
		else:
			x = 0*v7
			p9 = p9*1
			paths.append(2)
		if x <= 6:
			v7 = v7*1
			x = p9+6
			paths.append(3)
		else:
			p9 = p9/4
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))