import numpy as np 

def function(x):

	p5 = x
	d8 = 1
	paths = []
	try:
		if p5 < 1:
			d8 = d8-d8
			d8 = x-d8
			x = 3/9
			paths.append(1)
		else:
			d8 = x+x
			p5 = 3/9
			paths.append(2)
		if d8 > 7:
			d8 = 8+d8
			paths.append(3)
		else:
			x = d8*x
			x = 9/x
			p5 = p5*2
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		d8 = p5**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))