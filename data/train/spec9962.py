import numpy as np 

def function(x):

	b1 = x
	p5 = 8
	paths = []
	try:
		if b1 <= 1:
			x = b1*5
			p5 = p5/6
			x = 5*x
			paths.append(1)
		else:
			p5 = p5-9
			paths.append(2)
		if x > 6:
			b1 = b1*9
			paths.append(3)
		else:
			p5 = 5-3
			p5 = p5*1
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		b1 = p5**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))