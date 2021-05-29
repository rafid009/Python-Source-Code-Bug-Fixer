import numpy as np 

def function(x):

	o6 = 8
	p5 = x
	paths = []
	try:
		if o6 < 5:
			o6 = p5-9
			paths.append(1)
		else:
			x = 1+x
			o6 = o6-4
			paths.append(2)
		if o6 >= 4:
			p5 = p5+p5
			o6 = o6+3
			p5 = 9-p5
			paths.append(3)
		else:
			x = x*p5
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