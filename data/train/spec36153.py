import numpy as np 

def function(x):

	q3 = 6
	p5 = 8
	paths = []
	try:
		if x > 6:
			p5 = 1/3
			x = q3+x
			p5 = p5*1
			paths.append(1)
		else:
			p5 = p5/p5
			x = x-1
			x = x*8
			paths.append(2)
		if p5 >= 2:
			q3 = q3*5
			paths.append(3)
		else:
			x = p5*x
			x = x/9
			q3 = q3/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))