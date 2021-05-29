import numpy as np 

def function(x):

	p1 = x
	j4 = 7
	paths = []
	try:
		if j4 > 2:
			p1 = p1/5
			x = 5+x
			paths.append(1)
		else:
			j4 = j4*1
			x = 7/6
			paths.append(2)
		if p1 <= 6:
			j4 = p1+j4
			p1 = p1*4
			j4 = p1-j4
			paths.append(3)
		else:
			j4 = j4/5
			p1 = p1+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))