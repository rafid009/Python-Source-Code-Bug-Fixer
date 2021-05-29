import numpy as np 

def function(x):

	u9 = x
	p5 = 6
	paths = []
	try:
		if u9 < 3:
			x = 2*x
			p5 = p5/1
			paths.append(1)
		else:
			u9 = u9/u9
			paths.append(2)
		if p5 <= 7:
			u9 = u9+u9
			paths.append(3)
		else:
			p5 = 5*p5
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		p5 = u9**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))