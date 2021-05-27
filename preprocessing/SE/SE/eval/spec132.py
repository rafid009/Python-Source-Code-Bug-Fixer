import numpy as np 

def function(x):

	h1 = x
	p1 = x
	paths = []
	try:
		if h1 >= 4:
			x = h1*0
			p1 = 2+1
			paths.append(1)
		else:
			x = x-h1
			paths.append(2)
		if h1 > 4:
			x = x*x
			paths.append(3)
		else:
			p1 = h1*p1
			x = x*8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		p1 = h1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))