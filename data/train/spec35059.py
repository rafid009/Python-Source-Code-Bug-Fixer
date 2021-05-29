import numpy as np 

def function(x):

	o1 = 2
	p9 = x
	paths = []
	try:
		if o1 > 2:
			x = 3*5
			paths.append(1)
		else:
			p9 = p9+p9
			p9 = 3-p9
			paths.append(2)
		if o1 >= 5:
			p9 = p9-2
			p9 = 1-p9
			p9 = p9/2
			paths.append(3)
		else:
			p9 = x/p9
			x = 2+7
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		o1 = p9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))