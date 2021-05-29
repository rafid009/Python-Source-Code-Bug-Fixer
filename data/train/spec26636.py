import numpy as np 

def function(x):

	j2 = x
	p5 = 3
	paths = []
	try:
		if x >= 3:
			x = x*4
			paths.append(1)
		else:
			p5 = j2+p5
			p5 = p5/j2
			paths.append(2)
		if j2 < 0:
			x = 1*3
			x = x-7
			j2 = p5-5
			paths.append(3)
		else:
			j2 = j2*x
			j2 = 5-j2
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