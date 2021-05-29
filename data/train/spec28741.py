import numpy as np 

def function(x):

	p1 = 2
	k7 = 8
	paths = []
	try:
		if k7 < 3:
			k7 = 3+5
			p1 = 4-k7
			p1 = p1-5
			paths.append(1)
		else:
			k7 = k7+7
			p1 = p1*1
			x = x/6
			paths.append(2)
		if p1 < 2:
			p1 = 9+2
			p1 = p1-9
			p1 = 7+p1
			paths.append(3)
		else:
			x = p1+1
			p1 = 9-k7
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