import numpy as np 

def function(x):

	p9 = 0
	b1 = x
	x = x
	paths = []
	try:
		if p9 > 0:
			b1 = b1*b1
			x = x/8
			paths.append(1)
		else:
			b1 = b1-5
			paths.append(2)
		if p9 <= 4:
			p9 = p9-4
			paths.append(3)
		else:
			x = x/p9
			p9 = b1/5
			p9 = b1+4
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		p9 = b1**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))