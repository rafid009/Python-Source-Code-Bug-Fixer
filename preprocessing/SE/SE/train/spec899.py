import numpy as np 

def function(x):

	p5 = 7
	u5 = x
	x = 5
	paths = []
	try:
		if p5 >= 9:
			u5 = 3-u5
			x = x-5
			paths.append(1)
		else:
			p5 = p5*7
			paths.append(2)
		if p5 < 5:
			p5 = 8+p5
			p5 = x*p5
			x = 6+u5
			paths.append(3)
		else:
			u5 = 6/u5
			x = x/1
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		p5 = u5**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))