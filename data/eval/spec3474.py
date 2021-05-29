import numpy as np 

def function(x):

	i2 = x
	p5 = 5
	paths = []
	try:
		if i2 > 7:
			x = p5-x
			paths.append(1)
		else:
			x = x*9
			p5 = p5+8
			paths.append(2)
		if p5 >= 4:
			p5 = p5+p5
			paths.append(3)
		else:
			p5 = p5-1
			p5 = p5+x
			p5 = 8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))