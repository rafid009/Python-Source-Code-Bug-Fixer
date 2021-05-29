import numpy as np 

def function(x):

	p5 = 5
	n1 = x
	paths = []
	try:
		if p5 <= 5:
			n1 = n1*9
			x = 4+x
			paths.append(1)
		else:
			x = p5+x
			n1 = 0-n1
			paths.append(2)
		if p5 > 9:
			n1 = x*6
			p5 = 4-p5
			paths.append(3)
		else:
			x = x+5
			x = n1*1
			p5 = p5-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))