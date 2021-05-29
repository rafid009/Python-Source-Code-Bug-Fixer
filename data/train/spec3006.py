import numpy as np 

def function(x):

	p6 = x
	p9 = x
	paths = []
	try:
		if p9 > 7:
			p9 = p9/4
			p9 = p9-3
			p9 = x*p6
			paths.append(1)
		else:
			p9 = 4-p9
			paths.append(2)
		if p9 <= 2:
			x = 8-7
			x = 7+5
			p9 = x/p9
			paths.append(3)
		else:
			p6 = 8/5
			p6 = p9+p6
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))