import numpy as np 

def function(x):

	p5 = 3
	v4 = x
	paths = []
	try:
		if v4 >= 9:
			v4 = v4+0
			paths.append(1)
		else:
			v4 = 6*x
			x = 6+7
			paths.append(2)
		if x > 8:
			x = 0+9
			p5 = 4/p5
			paths.append(3)
		else:
			v4 = v4-0
			p5 = p5-2
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		p5 = v4**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))