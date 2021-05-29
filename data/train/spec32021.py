import numpy as np 

def function(x):

	p5 = 8
	t6 = x
	paths = []
	try:
		if t6 < 0:
			x = 7/x
			x = 9-x
			t6 = 9+t6
			paths.append(1)
		else:
			x = 4+p5
			paths.append(2)
		if t6 < 3:
			x = 6+t6
			t6 = 3*t6
			paths.append(3)
		else:
			x = t6/9
			x = x-9
			t6 = p5*t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))