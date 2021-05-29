import numpy as np 

def function(x):

	p9 = x
	e5 = x
	paths = []
	try:
		if e5 <= 8:
			e5 = 8-e5
			e5 = 4/e5
			x = x+1
			paths.append(1)
		else:
			e5 = p9-8
			p9 = 0-p9
			x = x/9
			paths.append(2)
		if e5 >= 7:
			x = x-e5
			p9 = p9+p9
			p9 = x/p9
			paths.append(3)
		else:
			p9 = 0-p9
			e5 = e5+7
			p9 = 8+p9
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