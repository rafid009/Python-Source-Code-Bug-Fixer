import numpy as np 

def function(x):

	p9 = x
	paths = []
	try:
		if p9 < 4:
			p9 = p9/x
			paths.append(1)
		else:
			p9 = p9/6
			p9 = 7/7
			p9 = p9/7
			paths.append(2)
		if p9 >= 0:
			p9 = x*p9
			paths.append(3)
		else:
			p9 = p9-3
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