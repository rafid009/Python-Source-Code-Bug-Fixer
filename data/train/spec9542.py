import numpy as np 

def function(x):

	k4 = 8
	p9 = x
	x = x
	paths = []
	try:
		if k4 > 5:
			x = x/p9
			paths.append(1)
		else:
			x = x+p9
			k4 = x-k4
			x = x/9
			paths.append(2)
		if p9 >= 4:
			x = 6*7
			x = 7*x
			p9 = 3*p9
			paths.append(3)
		else:
			p9 = 4+p9
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