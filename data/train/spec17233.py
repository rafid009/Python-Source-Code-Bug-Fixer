import numpy as np 

def function(x):

	p9 = 1
	j2 = x
	x = x
	paths = []
	try:
		if p9 <= 2:
			p9 = 6+p9
			x = 2*x
			paths.append(1)
		else:
			x = 6-x
			p9 = x+5
			p9 = x/p9
			paths.append(2)
		if j2 >= 6:
			p9 = p9-x
			p9 = 6*p9
			x = 9*4
			paths.append(3)
		else:
			p9 = p9-5
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