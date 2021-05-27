import numpy as np 

def function(x):

	j0 = 0
	p5 = 3
	paths = []
	try:
		if j0 <= 1:
			p5 = x-3
			j0 = 3-x
			p5 = j0+4
			paths.append(1)
		else:
			j0 = 0/5
			paths.append(2)
		if p5 <= 6:
			j0 = j0-2
			x = 8+x
			p5 = j0*1
			paths.append(3)
		else:
			x = x/7
			x = 0-p5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))