import numpy as np 

def function(x):

	i2 = x
	p5 = x
	paths = []
	try:
		if i2 < 1:
			p5 = p5/5
			i2 = p5-0
			i2 = 8-i2
			paths.append(1)
		else:
			p5 = 3+p5
			paths.append(2)
		if x > 0:
			i2 = 2/i2
			i2 = x-x
			paths.append(3)
		else:
			i2 = 0/i2
			i2 = 7*p5
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