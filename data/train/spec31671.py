import numpy as np 

def function(x):

	p2 = 2
	e2 = 0
	paths = []
	try:
		if e2 >= 9:
			p2 = p2*4
			paths.append(1)
		else:
			p2 = p2*0
			e2 = x*3
			paths.append(2)
		if e2 <= 1:
			e2 = e2-4
			p2 = p2+7
			paths.append(3)
		else:
			e2 = p2/6
			x = x*2
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		p2 = e2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))