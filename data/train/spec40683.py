import numpy as np 

def function(x):

	d5 = x
	p5 = x
	paths = []
	try:
		if p5 < 3:
			d5 = d5+x
			x = x/9
			paths.append(1)
		else:
			p5 = 1+p5
			p5 = d5+3
			p5 = p5-0
			paths.append(2)
		if d5 >= 4:
			x = x+3
			x = x/9
			paths.append(3)
		else:
			d5 = d5*4
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