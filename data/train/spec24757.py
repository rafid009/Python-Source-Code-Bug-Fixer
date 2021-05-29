import numpy as np 

def function(x):

	p5 = 9
	k6 = x
	paths = []
	try:
		if x <= 3:
			k6 = 5*k6
			paths.append(1)
		else:
			p5 = 2+p5
			k6 = k6*2
			p5 = 9-p5
			paths.append(2)
		if p5 > 2:
			p5 = p5-4
			x = 2+x
			p5 = k6-p5
			paths.append(3)
		else:
			p5 = 4/4
			x = 4+x
			k6 = 8/k6
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