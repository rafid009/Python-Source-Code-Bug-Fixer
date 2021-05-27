import numpy as np 

def function(x):

	v5 = x
	p5 = x
	paths = []
	try:
		if p5 >= 7:
			x = 1+2
			paths.append(1)
		else:
			v5 = 9-v5
			paths.append(2)
		if p5 <= 7:
			v5 = p5/9
			paths.append(3)
		else:
			v5 = 7/v5
			p5 = p5/p5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))