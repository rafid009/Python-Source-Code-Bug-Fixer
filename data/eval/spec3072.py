import numpy as np 

def function(x):

	p2 = x
	p9 = 5
	paths = []
	try:
		if p2 < 9:
			p2 = p9/x
			p9 = p9/1
			x = p9/2
			paths.append(1)
		else:
			p2 = 7+p2
			paths.append(2)
		if p9 < 7:
			x = 4/x
			paths.append(3)
		else:
			p9 = p9/5
			p9 = 4-4
			x = x*2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		x = p2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))