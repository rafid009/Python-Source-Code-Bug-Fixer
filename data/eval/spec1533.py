import numpy as np 

def function(x):

	p5 = 8
	w1 = x
	paths = []
	try:
		if p5 < 5:
			p5 = w1+p5
			w1 = 6*w1
			paths.append(1)
		else:
			p5 = 2/p5
			w1 = 4+w1
			p5 = 2-x
			paths.append(2)
		if x <= 7:
			p5 = 0-8
			w1 = w1+x
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		p5 = p5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))