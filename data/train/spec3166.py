import numpy as np 

def function(x):

	e1 = x
	p3 = x
	x = 5
	paths = []
	try:
		if p3 <= 3:
			e1 = e1+7
			p3 = p3/2
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if x < 0:
			e1 = e1*p3
			p3 = p3*5
			e1 = e1-5
			paths.append(3)
		else:
			e1 = x-9
			x = x+0
			p3 = p3*5
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		p3 = e1**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))