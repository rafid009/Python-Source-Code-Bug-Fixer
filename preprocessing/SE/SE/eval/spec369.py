import numpy as np 

def function(x):

	b9 = x
	p6 = x
	paths = []
	try:
		if x < 9:
			x = 3-b9
			p6 = p6*p6
			paths.append(1)
		else:
			p6 = p6*8
			paths.append(2)
		if b9 < 1:
			x = 4*x
			b9 = b9/9
			p6 = p6*2
			paths.append(3)
		else:
			p6 = p6*p6
			p6 = p6+p6
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		p6 = b9**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))