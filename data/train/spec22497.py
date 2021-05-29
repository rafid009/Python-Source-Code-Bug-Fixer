import numpy as np 

def function(x):

	p4 = 1
	b9 = x
	paths = []
	try:
		if p4 <= 4:
			b9 = b9+4
			x = b9/9
			x = 1/p4
			paths.append(1)
		else:
			x = 4+x
			x = p4*x
			paths.append(2)
		if b9 >= 5:
			p4 = p4/6
			p4 = p4*1
			x = 2*2
			paths.append(3)
		else:
			x = 7/p4
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))