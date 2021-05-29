import numpy as np 

def function(x):

	p1 = 2
	v2 = x
	paths = []
	try:
		if p1 < 3:
			x = 7-x
			x = x-7
			paths.append(1)
		else:
			x = x-8
			v2 = v2*4
			paths.append(2)
		if p1 < 7:
			x = 8+x
			x = x+7
			x = 6+1
			paths.append(3)
		else:
			x = x+5
			p1 = x-v2
			p1 = p1/x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		p1 = v2**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))