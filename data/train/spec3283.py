import numpy as np 

def function(x):

	p5 = 6
	r6 = 6
	paths = []
	try:
		if x <= 2:
			r6 = r6-r6
			p5 = x-p5
			p5 = 4/3
			paths.append(1)
		else:
			p5 = 0-p5
			x = x-x
			paths.append(2)
		if p5 < 2:
			p5 = 8+0
			r6 = 6-r6
			p5 = 0-2
			paths.append(3)
		else:
			r6 = r6-p5
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