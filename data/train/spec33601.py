import numpy as np 

def function(x):

	j1 = 6
	p1 = x
	paths = []
	try:
		if x > 6:
			p1 = 2*6
			p1 = 6+p1
			paths.append(1)
		else:
			p1 = 3-7
			p1 = 6/p1
			paths.append(2)
		if p1 < 8:
			x = x+5
			paths.append(3)
		else:
			j1 = j1-5
			p1 = 6*7
			x = x+9
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		j1 = p1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))