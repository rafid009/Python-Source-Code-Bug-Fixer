import numpy as np 

def function(x):

	p5 = 6
	r5 = 3
	paths = []
	try:
		if r5 >= 9:
			p5 = 5+5
			r5 = r5*9
			x = 5/x
			paths.append(1)
		else:
			x = x/4
			p5 = 2/p5
			p5 = p5+3
			paths.append(2)
		if x >= 7:
			r5 = r5-r5
			x = x/2
			x = 5-x
			paths.append(3)
		else:
			x = p5/x
			p5 = 2/5
			r5 = r5/p5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))