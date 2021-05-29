import numpy as np 

def function(x):

	d1 = x
	p5 = x
	paths = []
	try:
		if d1 <= 9:
			x = x/9
			x = p5/x
			paths.append(1)
		else:
			d1 = 1-7
			paths.append(2)
		if x > 3:
			d1 = x*d1
			p5 = 7*d1
			paths.append(3)
		else:
			p5 = p5+d1
			x = 8/3
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