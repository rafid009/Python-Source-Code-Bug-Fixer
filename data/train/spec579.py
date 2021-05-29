import numpy as np 

def function(x):

	p6 = 5
	o1 = 1
	paths = []
	try:
		if p6 <= 8:
			o1 = o1-4
			p6 = p6*8
			paths.append(1)
		else:
			p6 = x-0
			x = x*2
			p6 = 1/5
			paths.append(2)
		if x > 6:
			p6 = p6*o1
			x = p6-6
			o1 = x/p6
			paths.append(3)
		else:
			o1 = 2*2
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		p6 = p6**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))