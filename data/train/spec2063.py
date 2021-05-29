import numpy as np 

def function(x):

	p1 = x
	n2 = x
	paths = []
	try:
		if x > 4:
			n2 = 8-n2
			x = x-8
			paths.append(1)
		else:
			x = x/9
			p1 = p1/5
			x = 4/x
			paths.append(2)
		if n2 > 7:
			x = x*1
			n2 = 1/5
			paths.append(3)
		else:
			x = 8-7
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		n2 = p1**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))