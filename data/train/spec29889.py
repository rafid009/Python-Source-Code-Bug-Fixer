import numpy as np 

def function(x):

	p5 = x
	n5 = x
	x = 1
	paths = []
	try:
		if n5 <= 6:
			p5 = 1+p5
			n5 = n5/x
			paths.append(1)
		else:
			x = x+5
			p5 = 3+8
			x = n5/6
			paths.append(2)
		if p5 > 0:
			p5 = p5/5
			x = 1*n5
			paths.append(3)
		else:
			n5 = n5-p5
			x = x-2
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		p5 = n5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))