import numpy as np 

def function(x):

	u5 = 0
	p5 = x
	paths = []
	try:
		if p5 >= 9:
			u5 = u5*7
			p5 = x/5
			paths.append(1)
		else:
			u5 = x+u5
			p5 = 6*p5
			paths.append(2)
		if x <= 9:
			x = x-u5
			paths.append(3)
		else:
			p5 = p5-x
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		x = u5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))