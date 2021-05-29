import numpy as np 

def function(x):

	o6 = x
	p9 = x
	paths = []
	try:
		if x >= 1:
			x = 3*x
			x = 3*x
			paths.append(1)
		else:
			o6 = 8+o6
			x = x*2
			x = x/1
			paths.append(2)
		if p9 >= 7:
			x = o6-x
			paths.append(3)
		else:
			p9 = p9-7
			p9 = p9+9
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