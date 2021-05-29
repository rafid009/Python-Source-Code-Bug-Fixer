import numpy as np 

def function(x):

	p5 = x
	b4 = 6
	paths = []
	try:
		if b4 > 5:
			b4 = b4-7
			b4 = b4+7
			paths.append(1)
		else:
			p5 = b4/9
			paths.append(2)
		if x <= 9:
			x = b4-1
			b4 = 9/b4
			paths.append(3)
		else:
			x = 3*x
			b4 = b4/5
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