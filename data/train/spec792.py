import numpy as np 

def function(x):

	r1 = x
	p1 = x
	paths = []
	try:
		if p1 > 6:
			r1 = 2+x
			paths.append(1)
		else:
			r1 = r1/9
			x = x*3
			p1 = x+2
			paths.append(2)
		if p1 > 3:
			p1 = 9-x
			paths.append(3)
		else:
			p1 = 5-p1
			r1 = r1+x
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))