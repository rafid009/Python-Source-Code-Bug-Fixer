import numpy as np 

def function(x):

	p5 = x
	e6 = 7
	x = 9
	paths = []
	try:
		if x < 3:
			e6 = e6-2
			e6 = 8+x
			paths.append(1)
		else:
			x = 9-x
			paths.append(2)
		if x > 4:
			x = x-8
			e6 = e6+8
			e6 = 7-x
			paths.append(3)
		else:
			p5 = e6+p5
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		x = p5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))