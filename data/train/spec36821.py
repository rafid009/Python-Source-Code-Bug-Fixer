import numpy as np 

def function(x):

	p5 = 0
	i6 = x
	paths = []
	try:
		if p5 >= 5:
			i6 = 8-i6
			x = 0/i6
			paths.append(1)
		else:
			i6 = i6*9
			paths.append(2)
		if i6 < 3:
			x = x*3
			paths.append(3)
		else:
			x = 0+x
			p5 = p5-x
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