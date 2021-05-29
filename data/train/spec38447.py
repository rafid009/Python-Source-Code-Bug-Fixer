import numpy as np 

def function(x):

	p5 = 5
	o9 = x
	paths = []
	try:
		if x <= 4:
			x = 4/8
			paths.append(1)
		else:
			x = p5+x
			x = x-3
			paths.append(2)
		if p5 > 4:
			x = x/6
			paths.append(3)
		else:
			o9 = p5-7
			p5 = p5*x
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		x = o9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))