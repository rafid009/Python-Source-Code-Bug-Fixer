import numpy as np 

def function(x):

	p1 = x
	j9 = x
	paths = []
	try:
		if p1 > 3:
			j9 = x*5
			x = p1/x
			j9 = x-j9
			paths.append(1)
		else:
			x = x+6
			p1 = 8-p1
			p1 = 8/p1
			paths.append(2)
		if x <= 9:
			p1 = p1*x
			paths.append(3)
		else:
			x = 9-9
			p1 = p1+0
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		j9 = p1**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))