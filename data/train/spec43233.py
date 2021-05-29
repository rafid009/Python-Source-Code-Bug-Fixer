import numpy as np 

def function(x):

	f8 = 5
	p5 = x
	paths = []
	try:
		if p5 < 0:
			x = p5+f8
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if x < 6:
			x = 8-6
			p5 = p5-5
			paths.append(3)
		else:
			p5 = p5+p5
			f8 = f8+f8
			p5 = p5+x
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