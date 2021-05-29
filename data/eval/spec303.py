import numpy as np 

def function(x):

	p9 = x
	e2 = 2
	paths = []
	try:
		if p9 <= 9:
			e2 = p9-e2
			paths.append(1)
		else:
			e2 = e2-7
			paths.append(2)
		if x < 8:
			e2 = x+e2
			p9 = p9*3
			p9 = p9-e2
			paths.append(3)
		else:
			x = 8/2
			e2 = e2*6
			e2 = e2+6
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