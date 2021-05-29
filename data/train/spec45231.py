import numpy as np 

def function(x):

	o1 = x
	p5 = x
	paths = []
	try:
		if p5 > 3:
			x = x+7
			p5 = o1*p5
			x = x-3
			paths.append(1)
		else:
			o1 = 4+5
			o1 = 3/o1
			x = x*o1
			paths.append(2)
		if p5 > 5:
			o1 = 3-o1
			paths.append(3)
		else:
			x = x*8
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