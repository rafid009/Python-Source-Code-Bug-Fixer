import numpy as np 

def function(x):

	p5 = 6
	o6 = x
	paths = []
	try:
		if o6 < 5:
			o6 = o6+x
			x = x*7
			p5 = p5/7
			paths.append(1)
		else:
			p5 = p5*9
			p5 = 5/p5
			p5 = p5*p5
			paths.append(2)
		if o6 <= 5:
			o6 = o6-0
			p5 = p5*8
			paths.append(3)
		else:
			o6 = o6*2
			p5 = o6+1
			x = 0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))