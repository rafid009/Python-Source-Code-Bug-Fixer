import numpy as np 

def function(x):

	i3 = x
	p5 = x
	paths = []
	try:
		if p5 < 0:
			p5 = 1/p5
			p5 = 6+p5
			paths.append(1)
		else:
			p5 = p5-p5
			i3 = 4+i3
			paths.append(2)
		if p5 <= 6:
			p5 = 2+6
			paths.append(3)
		else:
			x = p5/x
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		p5 = i3**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))