import numpy as np 

def function(x):

	p9 = x
	a6 = 9
	x = x
	paths = []
	try:
		if p9 <= 7:
			x = x+6
			a6 = a6*6
			a6 = x/6
			paths.append(1)
		else:
			p9 = 3+p9
			p9 = p9+0
			paths.append(2)
		if x <= 3:
			x = x-2
			paths.append(3)
		else:
			a6 = x-8
			p9 = a6-a6
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		x = a6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))