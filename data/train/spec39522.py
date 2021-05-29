import numpy as np 

def function(x):

	p5 = x
	q2 = x
	x = 7
	paths = []
	try:
		if x < 9:
			x = x-0
			x = x*x
			paths.append(1)
		else:
			p5 = p5+x
			p5 = 7+p5
			paths.append(2)
		if q2 <= 6:
			x = 0*1
			p5 = 1/p5
			paths.append(3)
		else:
			x = 6/1
			p5 = p5*2
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