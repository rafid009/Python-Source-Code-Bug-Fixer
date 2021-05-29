import numpy as np 

def function(x):

	i5 = 0
	p5 = x
	x = 0
	paths = []
	try:
		if i5 < 7:
			i5 = 3+i5
			x = 3+x
			p5 = 4/p5
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if p5 > 0:
			p5 = p5+7
			paths.append(3)
		else:
			x = x*4
			i5 = 8-3
			paths.append(4)
		paths.append(5)
		assert p5 >= 0
		i5 = p5**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))