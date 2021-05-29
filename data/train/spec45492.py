import numpy as np 

def function(x):

	i3 = x
	p5 = 1
	paths = []
	try:
		if p5 >= 9:
			x = p5/x
			i3 = 7+i3
			paths.append(1)
		else:
			i3 = p5/6
			p5 = x+9
			paths.append(2)
		if x < 6:
			i3 = i3-i3
			i3 = i3/8
			paths.append(3)
		else:
			i3 = i3*x
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