import numpy as np 

def function(x):

	i9 = x
	p5 = 8
	paths = []
	try:
		if i9 <= 3:
			x = x*6
			i9 = 9*i9
			paths.append(1)
		else:
			i9 = x*1
			x = 5*5
			i9 = i9+9
			paths.append(2)
		if x <= 5:
			i9 = 8-i9
			i9 = 4-i9
			p5 = 9+7
			paths.append(3)
		else:
			i9 = i9*i9
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p5 = x**0.5
		return p5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))