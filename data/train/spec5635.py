import numpy as np 

def function(x):

	p5 = 8
	r8 = 4
	paths = []
	try:
		if x < 5:
			x = x/p5
			r8 = 7/r8
			paths.append(1)
		else:
			x = 4/x
			r8 = r8+0
			paths.append(2)
		if r8 < 8:
			r8 = 7+r8
			x = x*3
			paths.append(3)
		else:
			x = x+x
			p5 = p5-1
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